import time
from pathlib import Path
from pycromanager import Acquisition # type: ignore
from dask.distributed import Client, LocalCluster, Event, fire_and_forget
#from dask.distributed import print as dprint
#from rtseg.segmentation import cellsegment
#from rtseg.identify_channels import channel_locations
#from rtseg.forkplot import compute_forkplot_stats
#from rtseg.dotdetect import detect_dots

def acquire_events(acquisition, sim):

    def process_image(image, metadata):
        # submit the image to other places
        pass
    if sim:
        try:
            warmup_event = {
                'axes': {}, 
                'config_group': ['imaging', 'phase_fast'],
                'exposure': 0,
                'min_start_time': 0,
            }
            print(warmup_event)
            time.sleep(0.5)

            while not Event('kill_acquisition').is_set():
                time.sleep(0.5)
                print("Acquring next event: ", time.time())
        except KeyboardInterrupt:
            Event('kill_acquisition').set()
            print("Acquire process interrupted using keyboard")
        finally:
            # clean up the memory of the dask work loads 
            print("Acquire process completed successfully")
    else:
        try:
            with Acquisition(image_process_fn=process_image, show_display=False) as acq:
                acq.acquire(next(acquisition))
        except KeyboardInterrupt:
            Event('kill_acquisition').set()
            print("Acquire process interrupted using keyboard")
        finally:
            print("Acquire process completed successufully")



class ExptRun():

    def __init__(self, acquisition, save_dir, save):
        """
        Args:
            acquisition: has set of events, set in a loop with an iterator that you
                can use to iterate over
            save_dir: path of the directory to save images in 
            save: is true, then saves data to disk.
        """
        self.acquisition = acquisition
        self.save_dir = save_dir
        self.save = save

        expt_save_dir = Path(self.save_dir)
        if not expt_save_dir.exists():
            raise FileNotFoundError(f"Expt save directory {self.save_dir} doesn't exist")
        
        # initialize a dask cluster object and set some variables
        
        self.cluster = LocalCluster(n_workers=3, threads_per_worker=2)
        self.client = Client(self.cluster)

        # cluster wide variable, can be used to kill acquisition function
        self.acquire_kill =  Event('kill_acquisition')
        print("Prinitng events ... ")
        for event in self.acquisition.events:
            print(event)

    # submit to the cluster the acquisition of events.
    def start(self, acquisition, sim):
        future = self.client.submit(acquire_events, acquisition, sim)
        # will not wait for the result
        fire_and_forget(future)
        print("Submitted the task to dask cluster ...")
        

    # set the event to kill 
    def stop(self):
        
        if not self.acquire_kill.is_set():
            self.acquire_kill.set()
        
        time.sleep(1)
        print("Experiment stopped")
