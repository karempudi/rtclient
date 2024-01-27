import time
import logging
import logging.handlers
import multiprocessing as mp
import pathlib
from pathlib import Path

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

        logger = logging.getLogger(name)
        logger.log(logging.INFO, "Acquired sim ...")



    def acquire(self):
        self.setup_process_logger()
        name = mp.current_process().name 
        print(f"Starting {name} process ... ")

        logger = logging.getLogger(name)
        logger.log(logging.INFO, "Acquired real ...")
        self.acquire_kill.set()

    def segment(self):
        self.setup_process_logger()
        name = mp.current_process().name 
        print(f"Starting {name} process ... ")

        logger = logging.getLogger(name)
        logger.log(logging.INFO, "Segment img ...")
        self.segment_kill.set()



    def dots(self):
        self.setup_process_logger()
        name = mp.current_process().name 
        print(f"Starting {name} process ... ")

        logger = logging.getLogger(name)
        logger.log(logging.INFO, "Dots detected ...")
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
    