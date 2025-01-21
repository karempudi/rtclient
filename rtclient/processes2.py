import time
from pathlib import Path
from pycromanager import Acquisition # type: ignore
from dask.distributed import Client, LocalCluster, Event, fire_and_forget
from skimage.io import imread
from dask.distributed import print as dprint
from rtseg.identify_channels import get_barcode_model, detect_barcodes #type: ignore
#from rtseg.segmentation import cellsegment
#from rtseg.identify_channels import channel_locations
#from rtseg.forkplot import compute_forkplot_stats
#from rtseg.dotdetect import detect_dots

DUMMY_IMAGES_PATH = Path(__file__).parent / Path('resources/test_images')
DUMMY_IMAGES_PATH = DUMMY_IMAGES_PATH.resolve()
DUMMY_PHASE_PATH = DUMMY_IMAGES_PATH / Path('phase_dummy.tiff')
DUMMY_FLUOR_PATH = DUMMY_IMAGES_PATH / Path('fluor_dummy.tiff')

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

def get_dummy_phase():
    return imread(DUMMY_PHASE_PATH)

def get_dummy_fluor():
    return imread(DUMMY_FLUOR_PATH)

def acquire_events(events, sim, params, address):

    # segmentation model

    # Barcode model
    anchor_sizes = params.BarcodeAndChannels.model_params.anchors.sizes
    strides = params.BarcodeAndChannels.model_params.anchors.strides
    barcode_model, anchors, strides = get_barcode_model(params.BarcodeAndChannels.model_path, anchor_sizes, strides)
    barcode_model.share_memory()
    print("Barcode model loaded .... ")
 
    if sim:
        try:
            e = AcquisitionEvents(events)
            single_event = next(e)
            while not Event('kill_acquisition').is_set() and single_event is not None:
                if single_event['axes'] == {}:
                    print("Dummy position")
                elif single_event['axes']['preset'] == 'phase_fast':
                    phase_img = get_dummy_phase()
                    print(f"Acquired phase ({single_event['axes']['position']}) -- shape: {phase_img.shape}")
                    client = Client(address)
                    img1 = client.scatter(phase_img.astype('float32'))
                    barcodes_result = client.submit(detect_barcodes, barcode_model, anchors, strides, img1, [256, 800])
                    fire_and_forget(barcodes_result)
                    del img1
                elif single_event['axes']['preset'] == 'venus':
                    fluor_img = get_dummy_fluor()
                    print(f"Acquired venus ({single_event['axes']['position']}) -- shape: {fluor_img.shape}")
                single_event = next(e)
                time.sleep(0.5)
        except KeyboardInterrupt:
            Event('kill_acquisition').set()
            print("Acquire process interrupted using keyboard")
        finally:
            # clean up the memory of the dask work loads 
            print("Acquire process completed successfully")
    else:
        try:
            e = AcquisitionEvents(events)
            def process_image(image, metadata, event_queue):
                # submit the image to other places
                print(f'Image acquired: {image.shape}')
                #if not Event('kill_acquisition').is_set():
                next_event = next(e)
                event_queue.put(next_event)
                return 
            first_event = next(e)
            acq = Acquisition(name='test', image_process_fn=process_image, show_display=False)
            acq.acquire(first_event)
            acq.await_completion()
        except KeyboardInterrupt:
            Event('kill_acquisition').set()
            print("Acquire process interrupted using keyboard")
        finally:
            Event('kill_acquisition').set()
            print("Acquire process completed successufully")



class ExptRun():

    def __init__(self, acquisition, save_dir, params):
        """
        Args:
            acquisition: has set of events, set in a loop with an iterator that you
                can use to iterate over
            save_dir: path of the directory to save images in 
            save: is true, then saves data to disk.
        """
        self.acquisition = acquisition
        self.save_dir = save_dir
        self.params = params
        print(self.save_dir)
        self.params.Save.directory = str(self.save_dir)

        expt_save_dir = Path(self.save_dir)
        if not expt_save_dir.exists():
            raise FileNotFoundError(f"Expt save directory {self.save_dir} doesn't exist")
        
        # initialize a dask cluster object and set some variables
        
        self.cluster = LocalCluster(n_workers=3, threads_per_worker=2)
        self.client = Client(self.cluster)
        self.address = self.cluster.scheduler_address

        # cluster wide variable, can be used to kill acquisition function
        #acquire_kill =  Event('kill_acquisition')
        print("Prinitng events ... ")
        #for event in self.acquisition.events:
        #    print(event)

    # submit to the cluster the acquisition of events.
    def start(self, events, sim):
        future = self.client.submit(acquire_events, events, sim, self.params, self.address)
        # will not wait for the result
        fire_and_forget(future)
        dprint("Submitted the acquisition task to dask cluster ...")
        

    # set the event to kill 
    def stop(self):
        
        if not Event('kill_acquisition').is_set():
            Event('kill_acquisition').set()
        
        time.sleep(1)
        print("Experiment stopped")
