import sys
import numpy as np
import time
from pathlib import Path
#from pycromanager import Acquisition # type: ignore
from skimage.io import imread
import multiprocessing as mp
import logging
from rtclient.utils.logger import setup_root_logger

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
    def __init__(self, events):
        self.i = 0
        self.events = events
        self.max = len(self.events)

    def __next__(self):
        if self.i < self.max:
            event = self.events[self.i]
            self.i += 1
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
        self.expt_save_dir = self.params.Save.directory

        # create databases

        self.logger_queue = mp.Queue(-1)
        self.logger_kill_event = mp.Event()

        self.acquire_kill_event = mp.Event()
        self.acquire_queue = mp.Queue()

        self.segment_kill_event = mp.Event()
        self.segment_queue = mp.Queue()

        self.dots_kill_event = mp.Event()
        self.dots_queue = mp.Queue()


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

        e = AcquisitionEvents(self.events)
        data = None
        while not self.acquire_kill_event.is_set():
            try:
                next_event = next(e)
                if next_event is None:
                    data = None
                elif next_event['axes'] == {}:
                    data = {
                        'image': np.zeros((10, 10)),
                        'position': None,
                        'timepoint': None,
                        'chan': None
                    }
                elif next_event['axes']['preset'] == 'phase_fast':
                    data = {
                        'image': imread(DUMMY_PHASE_PATH),
                        'position': next_event['axes']['position'],
                        'timepoint': next_event['axes']['time'],
                        'chan': 'phase',
                    }
                elif next_event['axes']['preset'] == 'venus':
                    data = {
                        'image': imread(DUMMY_FLUOR_PATH),
                        'position': next_event['axes']['position'],
                        'timepoint': next_event['axes']['time'],
                        'chan': 'venus'
                    }

                if data is not None:
                    logger = logging.getLogger(name)
                    logger.log(logging.INFO, "Acquired image of shape: %s Pos: %s time: %s chan: %s",
                                data['image'].shape, data['position'], data['timepoint'], data['chan'])
                    self.segment_queue.put({
                        'position': data['position'],
                        'timepoint': data['timepoint'],
                        'image': data['image'],
                        'type': data['chan'],
                    })

                    # write to db that you acquired image

                else:
                    break
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
        pass

    def segment(self):
        self.set_process_logger()
        name = mp.current_process().name
        print(f"Starting {name} process ..")

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

                # write to database that we processes something

                # put the result in  dots queue for further processing

                logger = logging.getLogger(name)
                logger.log(logging.INFO, "Segmented Pos: %s, time: %s chan: %s", 
                            data_seg_queue['position'], data_seg_queue['timepoint'], data_seg_queue['type'])

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

                # write to db that you are done dot calcuation 

                # logging 
                logger = logging.getLogger(name)
                logger.log(logging.INFO, "Dots queue  got Pos: %s time %s", 
                                data_dots_queue['position'],
                                data_dots_queue['time'])
                
            except KeyboardInterrupt:
                self.acquire_kill_event.set()
                sys.stdout.write("Dots process interrupted using keyboard\n")
                sys.stdout.flush()
                break
        
        self.dots_kill_event.set()
        sys.stdout.write("Dots process completed successfully\n")
        sys.stdout.flush()

    def stop(self):
        if not self.acquire_kill_event.is_set():
            self.acquire_kill_event.set()
        
        while ((not self.segment_kill_event.is_set()) or (not self.dots_kill_event.is_set())):
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

    except KeyboardInterrupt:
        pass

