import sys
import numpy as np
import time
from pathlib import Path
from pycromanager import Acquisition # type: ignore
from skimage.io import imread
import multiprocessing as mp
import logging
from rtclient.utils.logger import setup_root_logger
from rtseg.segmentation import get_live_model, live_segment
from rtseg.dotdetect import compute_dot_coordinates
from rtseg.forkplot import compute_forkplot_stats
from rtseg.utils.db_ops import create_databases, write_to_db
from rtseg.utils.param_io import save_params
from rtseg.utils.disk_ops import write_files

DUMMY_IMAGES_PATH = Path(__file__).parent / Path('resources/test_images')
DUMMY_IMAGES_PATH = DUMMY_IMAGES_PATH.resolve()
DUMMY_PHASE_PATH = DUMMY_IMAGES_PATH / Path('phase_dummy.tiff')
DUMMY_FLUOR_PATH = DUMMY_IMAGES_PATH / Path('fluor_dummy.tiff')

def worker_configurer(queue):
    h = logging.handlers.QueueHandler(queue)
    root = logging.getLogger()
    root.addHandler(h)
    root.setLevel(logging.DEBUG)

def worker_process(queue, configurer):
    configurer(queue)

class AcquisitionEvents:
    def __init__(self, events, cycle_no=0, min_start_time=0):
        self.i = 0
        self.events = events
        for event in self.events:
            event['min_start_time'] = min_start_time
            event['axes']['time'] = cycle_no
        self.max = len(self.events)

    def __next__(self):
        if self.i < self.max:
            event = self.events[self.i]
            self.i += 1
            return event
        else:
            return None

class AcquisitionEventsSim:
    def __init__(self, events, cylce_no=0, min_start_time=0):
        self.i = 0
        self.events = events
        for event in self.events:
            event['min_start_time'] = min_start_time
            event['axes']['time'] = cylce_no
        self.max = len(self.events)

    def __next__(self):
        if self.i < self.max:
            event = self.events[self.i:self.i+2]
            self.i += 2
            return event
        else:
            return None



class ExptRun:
    """
    Experiment run object that hold all the queues for 
    managing the data produced during the run and process them
    appropriately, based on the settings provided by the parameter
    file.
    """ 
    def __init__(self, params, events):
        self.params = params
        self.events = events
        self.expt_save_dir = Path(str(self.params.Save.directory))


        # save parameters used
        save_param_path = self.expt_save_dir / Path('param_used.yaml')
        save_params(save_param_path, self.params)

        # create databases

        create_databases(self.expt_save_dir, ['acquire_phase', 'acquire_fluor', 'segment'])

        self.logger_queue = mp.Queue(-1)
        self.logger_kill_event = mp.Event()

        self.acquire_kill_event = mp.Event()
        self.acquire_queue = mp.Queue()

        self.segment_kill_event = mp.Event()
        self.segment_queue = mp.Queue()

        self.dots_kill_event = mp.Event()
        self.dots_queue = mp.Queue()

        self.internal_kill_event = mp.Event()
        self.internal_queue = mp.Queue()


    def logger_listener(self):
        setup_root_logger(self.params, self.expt_save_dir)
        name = mp.current_process().name
        print(f"Starting {name} process ..")
        while not self.logger_kill_event.is_set():
            try:
                record = self.logger_queue.get()
                if record is None:
                    break
                logger = logging.getLogger(record.name)
                logger.handle(record)

            except KeyboardInterrupt:
                self.logger_kill_event.set()
                sys.stdout.write("Logger process interrupted using keyboard\n")
                sys.stdout.flush()
                break

    def set_process_logger(self):
        h = logging.handlers.QueueHandler(self.logger_queue)
        root = logging.getLogger()
        root.addHandler(h)
        root.setLevel(logging.DEBUG)

    def acquire_sim(self):
        self.set_process_logger()
        name = mp.current_process().name
        print(f"Starting {name} process ...")
        current_cycle_no = 0
        max_cycles = 1
        e = AcquisitionEventsSim(self.events, current_cycle_no)
        data = None
        time.sleep(4)
        while not self.acquire_kill_event.is_set():
            try:
                next_event = next(e)
                if next_event is None:
                    print("Got None in next event")
                    data = None
                elif next_event[0]['axes'] == {}:
                    data = {
                        'phase': np.zeros((10, 10)),
                        'fluor': np.zeros((10, 10)),
                        'position': None,
                        'timepoint': None,
                        'chan': None
                    }
                elif next_event[0]['axes']['preset'] == 'phase_fast' and next_event[1]['axes']['preset'] == 'venus':
                    data = {
                        'phase': imread(DUMMY_PHASE_PATH),
                        'fluor': imread(DUMMY_FLUOR_PATH),
                        'position': next_event[0]['axes']['position'],
                        'timepoint': next_event[0]['axes']['time'],
                        'chan': 'phase_fluor',
                    }

                if data is not None:
                    logger = logging.getLogger(name)
                    logger.log(logging.INFO, "Acquired phase img shape: %s fluor shape: %s, Pos: %s time: %s chan: %s",
                                data['phase'].shape, data['fluor'].shape, data['position'], data['timepoint'], data['chan'])
                    self.segment_queue.put({
                        'position': data['position'],
                        'timepoint': data['timepoint'],
                        'phase': data['phase'],
                        'fluor': data['fluor'],
                        'type': data['chan'],
                    })

                    # write to db that you acquired image
                    write_to_db({
                        'position': data['position'],
                        'timepoint': data['timepoint']}, self.expt_save_dir, 'acquire_phase')
                    write_to_db({'position': data['position'],
                            'timepoint': data['timepoint']}, self.expt_save_dir, 'acquire_fluor')

                else:
                    if current_cycle_no == max_cycles:
                        break
                    current_cycle_no += 1
                    e = AcquisitionEventsSim(self.events, current_cycle_no, 0)
                time.sleep(0.50)
            except KeyboardInterrupt:
                self.acquire_kill_event.set()
                sys.stdout.write("Acquire process interrupted using keyboard\n")
                sys.stdout.flush()
                break
        
        self.segment_queue.put(None)
        sys.stdout.write("Acquire sim process completed successfully\n")
        sys.stdout.flush()

    def acquire(self):
        self.set_process_logger()
        name = mp.current_process().name
        print(f"Starting {name} process ..")
        self.current_cycle_no = 0
        self.max_cycles = 90
        self.cycle_time = 120
        self.e = AcquisitionEvents(self.events, self.current_cycle_no)

        time.sleep(4)


        def put_images_in_queue(image, metadata, event_queue):
            #print(metadata['Axes'], '----->', image.shape)

            if not hasattr(put_images_in_queue, 'datapoint'):
                put_images_in_queue.datapoint = {}

            img_type = metadata['Axes']['preset']
            if img_type == 'phase_fast':
                key = 'phase'
            elif img_type == 'venus':
                key = 'fluor'
                
            put_images_in_queue.datapoint[key] = image
            put_images_in_queue.datapoint['position'] = metadata['Axes']['position']
            put_images_in_queue.datapoint['timepoint'] = metadata['Axes']['time']

            #print(put_images_in_queue.datapoint.keys())

            if 'phase' in put_images_in_queue.datapoint.keys() and 'fluor' in put_images_in_queue.datapoint.keys():
                put_images_in_queue.datapoint['type'] = 'phase_fluor'

                data = put_images_in_queue.datapoint
                logger = logging.getLogger(name)
                logger.log(logging.INFO, "Acquired phase img shape: %s fluor shape: %s, Pos: %s time: %s chan: %s",
                                data['phase'].shape, data['fluor'].shape, data['position'], data['timepoint'], data['type'])
                self.segment_queue.put(data)
                #print('Put a datapoint in the queue')
                put_images_in_queue.datapoint = {}
            

            next_event = next(self.e)
            if next_event is None:
                if self.current_cycle_no == self.max_cycles:
                    next_event = None
                else:
                    self.current_cycle_no += 1
                    self.e = AcquisitionEvents(self.events, self.current_cycle_no, self.current_cycle_no * self.cycle_time)
                    next_event = next(self.e)
            #print(f"Next event: {next_event}")
            event_queue.put(next_event)
            return 
        acq = Acquisition(name='acquire_one_loop', image_process_fn=put_images_in_queue, show_display=False)
        acq.acquire(next(self.e))
        acq.await_completion()

                
        self.segment_queue.put(None)
        sys.stdout.write("Acquire real process completed successfully\n")
        sys.stdout.flush()
        

    def segment(self):
        self.set_process_logger()
        name = mp.current_process().name
        print(f"Starting {name} process ..")

        # Load network
        net = get_live_model(self.params)

        while True:
            try:
                if self.segment_queue.qsize() > 0:
                    data_seg_queue = self.segment_queue.get()
                    if data_seg_queue is None:
                        sys.stdout.write("Got None in seg image queue .. aborting segment function ..\n")
                        sys.stdout.flush()
                        break
                else:
                    continue

                # do something with the image ... process or something
                if data_seg_queue['type'] is not None:

                    seg_result = live_segment(data_seg_queue, net, self.params)

                    # write files now
                    write_files({
                        'position': seg_result['position'],
                        'image': seg_result['phase'],
                        'timepoint': seg_result['timepoint'],
                    }, 'phase', self.params)

                    write_files({
                        'position': seg_result['position'],
                        'image': seg_result['fluor'],
                        'timepoint': seg_result['timepoint'],
                    }, 'fluor', self.params)

                    write_files({
                        'position': seg_result['position'],
                        'image': seg_result['seg_mask'],
                        'timepoint': seg_result['timepoint'],
                    }, 'seg_mask', self.params)

                    write_files({
                        'position': seg_result['position'],
                        'image': seg_result['seg_mask'],
                        'timepoint': seg_result['timepoint'],
                        'trap_locations_list': seg_result['trap_locations_list'],
                    }, 'segmented_cells_by_trap', self.params)

                    # write to database that we processes something and also barcodes and channel locations
                    
                    write_to_db(seg_result, self.expt_save_dir, 'segment')

                    # logging  
                    logger = logging.getLogger(name)
                    logger.log(logging.INFO, "Segmented Pos: %s, time: %s chan: %s, result: %s, bboxes: %s, num_traps: %s", 
                                data_seg_queue['position'], data_seg_queue['timepoint'], data_seg_queue['type'],
                                seg_result['seg_mask'].shape, len(seg_result['barcode_locations']), seg_result['num_traps'])

                    # put the result in  dots queue for further processing
                    self.dots_queue.put({
                        'position': data_seg_queue['position'],
                        'timepoint': data_seg_queue['timepoint'],
                        'seg_mask': seg_result['seg_mask'],
                        'fluor': seg_result['fluor'],
                        # needs channel locations to cut dots by trap
                        'trap_locations_list': seg_result['trap_locations_list']
                    })

            except KeyboardInterrupt:
                self.acquire_kill_event.set()
                sys.stdout.write("Segment process interrupted using keyboard\n")
                sys.stdout.flush()
                break
        
        self.dots_queue.put(None)
        self.segment_kill_event.set()
        sys.stdout.write("Segment process completed sucessfully\n")
        sys.stdout.flush()


    def dots(self):
        self.set_process_logger()
        name = mp.current_process().name
        print(f"Starting {name} process ..")

        while True:
            try:
                if self.dots_queue.qsize() > 0:
                    data_dots_queue = self.dots_queue.get()
                    if data_dots_queue is None:
                        sys.stdout.write("Got None in dots queue .. aborting dots function ...\n")
                        sys.stdout.flush()
                        break
                else:
                    continue
                
                # write code to call dots calculation here
                dots_on_image  = compute_dot_coordinates(data_dots_queue['fluor'],
                                            data_dots_queue['seg_mask'], self.params)


                # write to db that you are done dot calcuation 


                # write dot results
                write_files({'position': data_dots_queue['position'],
                             'timepoint': data_dots_queue['timepoint'],
                             'raw_coords': dots_on_image['raw_coords'],
                             'rotated_coords': dots_on_image['rotated_coords']},
                             'dot_coordinates', self.params)


                # send of the results towards calculating internal coordinates
                self.internal_queue.put({
                    'seg_mask': data_dots_queue['seg_mask'],
                    'rotated_coords': dots_on_image['rotated_coords'],
                    'position': data_dots_queue['position'],
                    'timepoint': data_dots_queue['timepoint'],
                    'trap_locations_list': data_dots_queue['trap_locations_list'],
                })

                # logging 
                logger = logging.getLogger(name)
                logger.log(logging.INFO, "Dots queue  got Pos: %s time %s dots: %s", 
                                data_dots_queue['position'],
                                data_dots_queue['timepoint'], dots_on_image['raw_coords'].shape)
                
            except KeyboardInterrupt:
                self.acquire_kill_event.set()
                sys.stdout.write("Dots process interrupted using keyboard\n")
                sys.stdout.flush()
                break

        self.internal_queue.put(None)
        self.dots_kill_event.set()
        sys.stdout.write("Dots process completed successfully\n")
        sys.stdout.flush()


    def internal(self):
        self.set_process_logger()
        name = mp.current_process().name
        print(f"Starting {name} process ..")

        while True:
            try:
                if self.internal_queue.qsize() > 0:
                    data_internal_queue = self.internal_queue.get()
                    if data_internal_queue is None:
                        sys.stdout.write("Got None in internal queue .. aborting internal function ...\n")
                        sys.stdout.flush()
                        break
                else:
                    continue

                # computer internal coordinates using props and backbone fits
                forkplot_data = compute_forkplot_stats(data_internal_queue['seg_mask'], 
                                        data_internal_queue['rotated_coords'],
                                        data_internal_queue['position'],
                                        data_internal_queue['timepoint'],
                                        data_internal_queue['trap_locations_list'])
                
                # write results
                write_files({
                    'position': data_internal_queue['position'],
                    'timepoint': data_internal_queue['timepoint'],
                    'fork_data': forkplot_data
                }, 'forkplot_data', self.params)

                # write to db

 
                # logging 
                logger = logging.getLogger(name)
                logger.log(logging.INFO, "Internal queue  got Pos: %s time %s dots: %s, traps: %s, forks: %s", 
                                data_internal_queue['position'],
                                data_internal_queue['timepoint'], 
                                data_internal_queue['rotated_coords'].shape, len(data_internal_queue['trap_locations_list']),
                                len(forkplot_data))
                    
            except KeyboardInterrupt:
                self.acquire_kill_event.set()
                sys.stdout.write("Internal process interrupted using keyboard\n")
                sys.stdout.flush()
                break
        
        self.internal_kill_event.set()
        sys.stdout.write("Internal process completed successfully\n")
        sys.stdout.flush()


    def stop(self):
        if not self.acquire_kill_event.is_set():
            self.acquire_kill_event.set()
        
        while ((not self.segment_kill_event.is_set()) or (not self.dots_kill_event.is_set()) or (not self.internal_kill_event.is_set())):
            time.sleep(1)
        self.logger_queue.put(None)
        time.sleep(1)
        self.logger_kill_event.set()
    

def start_live_experiment(expt_run, sim = False):

    mp.freeze_support()
    try:
        mp.set_start_method('spawn')
    except Exception:
        pass

    try:
        expt_run.logger_kill_event.clear()
        logger_process = mp.Process(target=expt_run.logger_listener, name='logger')
        logger_process.start()

        # acquire process

        expt_run.acquire_kill_event.clear()
        if sim:
            acquire_process = mp.Process(target=expt_run.acquire_sim, name='acquire_sim')
        else:
            acquire_process = mp.Process(target=expt_run.acquire, name='acquire')
        acquire_process.start()

        # segment process

        expt_run.segment_kill_event.clear()
        segment_process = mp.Process(target=expt_run.segment, name='segment')
        segment_process.start()

        # dots process
        
        expt_run.dots_kill_event.clear()
        dots_process = mp.Process(target=expt_run.dots, name='dots')
        dots_process.start()


        # internal coordinates process
        expt_run.internal_kill_event.clear()
        internal_process = mp.Process(target=expt_run.internal, name='internal')
        internal_process.start()

    except KeyboardInterrupt:
        pass

