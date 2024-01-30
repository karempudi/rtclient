import time
import logging
import logging.handlers
import multiprocessing as mp
import pathlib
from pathlib import Path
from pycromanager import Acquisition # type: ignore
from skimage.io import imread

RESOURES_PATH = Path(__file__).parent / Path('./resources/test_images/')
RESOURES_PATH = RESOURES_PATH.resolve()
DUMMY_PHASE = "phase.jpg"

def send_phase_image(data): 
    return {'error': True}

def send_dots_image(data):
    return {'error': True}

def setup_root_logger(save_dir):
    """
    write the logs to a log file in the saving directory

    """
    if isinstance(save_dir, str):
        save_dir = Path(save_dir)
    assert isinstance(save_dir, pathlib.Path)
    root = logging.getLogger()
    f = logging.Formatter('%(asctime)s %(processName)-10s %(levelname)-8s %(message)s')
    
    logging_directory = save_dir / Path('logs.log')
    h = logging.FileHandler(filename=logging_directory, mode='w')
    h.setFormatter(f)
    root.addHandler(h)

    c = logging.StreamHandler()
    c.setFormatter(f)
    root.addHandler(c)


class ExptRun():
    
    def __init__(self, acquisition, save_dir):
        self.acquisition = acquisition
        self.save_dir = save_dir

        expt_save_dir = Path(self.save_dir) 
        if not expt_save_dir.exists():
            raise FileNotFoundError(f"Experiment save directory {self.save_dir} doesn't exist \n")

        self.acquire_kill = mp.Event()

        self.logger_queue = mp.Queue()
        self.logger_kill = mp.Event()

        self.segment_queue = mp.Queue()
        self.segment_kill = mp.Event()

        self.dots_queue = mp.Queue()
        self.dots_kill = mp.Event()
        
    def setup_process_logger(self):
        h = logging.handlers.QueueHandler(self.logger_queue)
        root = logging.getLogger()
        root.addHandler(h)
        root.setLevel(logging.DEBUG)
    
    def logger_listener(self):
        setup_root_logger(self.save_dir)
        name = mp.current_process().name
        print(f"Starting {name} process ..")
        while not self.logger_kill.is_set():
            try:
                record = self.logger_queue.get()
                if record is None:
                    break
                logger = logging.getLogger(record.name)
                logger.handle(record)

            except KeyboardInterrupt:
                self.logger_kill.set()
                print('Logger process interrupted using keyboard')
                break
    
    def acquire_sim(self):
        self.setup_process_logger()
        name = mp.current_process().name 
        print(f"Starting {name} process ... ")
        # put the dummy phase and fluor image in different queues
        phase_path = RESOURES_PATH / Path(DUMMY_PHASE)
        dummy_phase = imread(phase_path).astype('float32')
        dummy_fluor = imread(phase_path).astype('float32')
        def put_image_queue(image, metadata, event_queue):
            pass

        while not self.acquire_kill.is_set():
            try:
                # acquire and put two image in different queues
                event = next(self.acquisition)
                time.sleep(1)
                logger = logging.getLogger(name)
                if event['config_group'][1] == 'phase_fast':
                    self.segment_queue.put({
                        'position': 1,
                        'time': 0,
                        'image': dummy_phase
                    })
                    logger.log(logging.INFO, "Acquired phase image Pos: %s Time: %s", 1, 0)
                if event['config_group'][1] == 'venus':
                    self.dots_queue.put({
                        'position': 1,
                        'time': 0,
                        'image': dummy_fluor
                    })
                    logger.log(logging.INFO, "Acquired fluor image Pos: %s Time: %s", 1, 0)
            except KeyboardInterrupt:
                self.acquire_kill.set()
                print("Acquire process interrupted using keyboard")
                break
            except Exception as e:
                print(f"Error {e} in acquire sim")
        
        self.segment_queue.put(None)
        self.dots_queue.put(None)
        print("Acquire sim process completed successfully")


    def acquire(self):
        self.setup_process_logger()
        name = mp.current_process().name 
        print(f"Starting {name} process ... ")

        def put_image_in_queue(image, metadata, event_queue):
            
            # put image in different queues depending on the type of image
            # acquired
            self.segment_queue.put({
                'position': metadata['Axes']['position'],
                'time': metadata['Axes']['time'],
                'image': image.astype('float32')
            })

            logger = logging.getLogger('acquire')
            logger.log(logging.INFO, "Acquired image of position: %s, time: %s",
                        metadata['Axes']['position'], metadata['Axes']['time'])
            
            if self.acquire_kill.is_set():
                event_queue.put(None)
            else:
                event_queue.put(next(self.acquisition))

        try:
            event = next(self.acquisition)
            with Acquisition(image_process_fn=put_image_in_queue, show_display=False) as acq:
                acq.acquire(event)

        except KeyboardInterrupt:
            self.acquire_kill.set()
            print("Acquire process interrupted using keyboard")
        finally:
            self.segment_queue.put(None)
            print("Acquire process completed successfully")
    

    def segment(self):
        self.setup_process_logger()
        name = mp.current_process().name 
        print(f"Starting {name} process ... ")

        while True:
            try:
                if self.segment_queue.qsize() > 0:
                    data_in_seg_queue = self.segment_queue.get()
                    if data_in_seg_queue is None:
                        print("Got None in segementation image queue .. aborting segmentation function")
                        break
                else:
                    continue
                
                try:
                    seg_result = send_phase_image(data_in_seg_queue)
                except Exception as e:
                    print(f"Error {e} while sending image from segmentation queue")

                logger = logging.getLogger(name)
                logger.log(logging.INFO, "Segmented img Pos: %s, time: %s, error: %s sent",
                            data_in_seg_queue['position'],
                            data_in_seg_queue['time'], seg_result['error'])
            except KeyboardInterrupt:
                self.acquire_kill.set()
                print("Segmentation process interrupted using keyboard")
                break
            
        self.segment_kill.set()

    def dots(self):
        self.setup_process_logger()
        name = mp.current_process().name 
        print(f"Starting {name} process ... ")
        while True:
            try:
                if self.dots_queue.qsize() > 0:
                    data_in_dots_queue = self.dots_queue.get()
                    if data_in_dots_queue is None:
                        print("Got None in dots image queue .. aborting dots function")
                        break
                else:
                    # you can time.sleep(1) for a bit here
                    continue 

                try:
                    dots_result = send_dots_image(data_in_dots_queue)
                except Exception as e:
                    print(f"Erro {e} while sending image form dots queue")

                logger = logging.getLogger(name)
                logger.log(logging.INFO, "Dots img Pos:%s, time: %s, error: %s sent",
                            data_in_dots_queue['position'],
                            data_in_dots_queue['time'],
                            dots_result['error'])

            except KeyboardInterrupt:
                self.acquire_kill.set()
                print("Dots process interrupted using keyboard")
                break

        self.dots_kill.set()

    def stop(self):

        if not self.acquire_kill.is_set():
            self.acquire_kill.set()

        while ((not self.segment_kill.is_set()) or (not self.dots_kill.is_set())):
            time.sleep(1)

        self.logger_queue.put(None)
        time.sleep(1)
        self.logger_kill.set()
        print("Experiment stopped")

def start_experiment(expt_run, sim: bool = False):
    """
    Function that starts the processes that dispatch images else where 
    from the queues that are present in the expt run object

    Args:
        expt_run (ExptRun): an instance of experiment run object that
            handles all the events to acquire and all the keys 
        sim (bool): if set then tries to do a real experiment acqusition
                    otherwise reads the experiment data from disk

    """
    mp.freeze_support()
    try:
        mp.set_start_method('spawn')
    except Exception:
        pass

    # Set up processes for each of the functions you want to run

    try:
        expt_run.logger_kill.clear()
        logger_process = mp.Process(target=expt_run.logger_listener, name='logger')
        logger_process.start()

        # acquire images 
        expt_run.acquire_kill.clear()

        if sim:
            acquire_process = mp.Process(target=expt_run.acquire_sim, name='acquire_sim')
        else:
            acquire_process = mp.Process(target=expt_run.acquire, name='acquire')
        acquire_process.start()

        expt_run.segment_kill.clear()
        segment_process = mp.Process(target=expt_run.segment, name='segment')
        segment_process.start()

        expt_run.dots_kill.clear()
        dots_process = mp.Process(target=expt_run.dots, name='dots')
        dots_process.start()
        

    except KeyboardInterrupt:
        pass
    