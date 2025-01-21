import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import Slot
from rtclient.ui.qt_ui_classes.ui_main import Ui_MainWindow
from rtclient.ui.positions_window import PositionsWindow
from rtclient.ui.tweezer_window import TweezerWindow
from rtclient.ui.preview_window import PreviewWindow
#from rtclient.microscope.acquisition import Acquisition
#from rtclient.processes2 import ExptRun
from rtseg.utils.param_io import load_params, save_params # type: ignore
from copy import deepcopy
import json
from pathlib import Path


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.positions_window = PositionsWindow()
        self.tweezer_window = TweezerWindow()
        self.preview_window = PreviewWindow()

        self.selected_values = None
        self.simulated_acquisition = False
        self.save_dir = None
        self.analysis_params = None
        self.events = None

        self.setup_button_handlers()


    def setup_button_handlers(self):

        self._ui.positions_button.clicked.connect(self.show_positions_window)
        self._ui.rules_button.clicked.connect(self.show_positions_window)
        self._ui.preview_button.clicked.connect(self.show_preview_window)
        self.positions_window.send_events.connect(self.generate_run_params)


        self._ui.tweezer_button.clicked.connect(self.show_tweezer_window)

        self._ui.parameters_button.clicked.connect(self.load_analysis_parameters)

        self._ui.write_run_params_button.clicked.connect(self.write_run_params)

        self._ui.load_run_params_button.clicked.connect(self.load_run_params)

        self._ui.quit_button.clicked.connect(self.closeEvent)
    
    @Slot()
    def show_positions_window(self):
        self.positions_window.show()
    
    @Slot()
    def show_tweezer_window(self):
        self.tweezer_window.show()
    
    @Slot()
    def show_preview_window(self):
        self.preview_window.show()
        if self.selected_values is None:
            msg = QMessageBox()
            msg.setText('Events not set, so no preview')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        else:
            events = self.selected_values['events']
            self.preview_window._ui.preview_list.clear()
            for event in events:
                self.preview_window._ui.preview_list.addItem('Pos' + str(event['extra_tags']['position']) + ',' 
                            + event['config_group'][0] + ',' + event['config_group'][1] + ', '
                            + str(event['exposure']) + 'ms')

    @Slot()
    def load_analysis_parameters(self):
        print("Loading analysis parameters .....")
        # open file dialog and load a yaml file containing parameters for analysis
        try:
            filename, _ = QFileDialog.getOpenFileName(self,
                                self.tr("Open analysis parameter yaml file"),
                                '../rtseg/rtseg/resources/reference_params',
                                self.tr("yaml file (*.yaml *.yml)"))
            if filename == '':
                msg = QMessageBox()
                msg.setText("Analysis paramters not selected")
                msg.exec()
            else:
                #load params
                self.params = load_params(filename, ref_type='expt')
        except Exception as e:
            sys.stdout.write(f"Error in loading analysis setup file --- {e}\n")
            sys.stdout.flush()
        
        finally:
            if self.params is not None:
                sys.stdout.write("Parameters for analysis set from file. \n")
                sys.stdout.flush()
                print("--------- Params ------------")
                print(self.params)
                print("----------------------------")
        
    
    def closeEvent(self, event):
        self.tweezer_window.close()
        self.positions_window.close()
        sys.exit()

    def generate_run_params(self, selected_values):
        self.selected_values = selected_values
        self.events = selected_values['events']
        self.save_dir = selected_values['save_dir']
        self.simulated_acquisition = selected_values['simulated_acquisition']

    def write_run_params(self):
        self.analysis_params = self.params
        write_params = deepcopy(self.analysis_params)
        write_params.Save.directory = str(self.save_dir)
        write_params.Save.sim = self.simulated_acquisition


        # write events to json file in the save directory
        events_path = Path(str(self.save_dir)) / Path('events.json')
        with open(events_path, 'w') as fp:
            json.dump(self.events, fp)

        write_params.Events.path = str(Path(str(self.save_dir)) / Path('events.json'))
        
        # select a directory and write params to file
        save_path = Path(write_params.Save.directory) / Path('expt_params.yaml')
        save_params(save_path, write_params)

        print(f"Writing parameters to path {str(save_path)}")

    def load_run_params(self):
        pass
   
    #def create_acquisition(self, selected_values):
    #    self.selected_values = selected_values
    #    #print("Events list recieved.. constructing acquisition object: ", len(selected_values['events']))
    #    self.acquisition = Acquisition(selected_values['events'])
    #    self.save_dir = selected_values['save_dir']
    #    self.simulated_acquisition = selected_values['simulated_acquisition']
    #   #print("Acquisition object set")
    #    print(f"Acquisition object set with {len(selected_values['events'])} events, simulated: {selected_values['simulated_acquisition']}")

    #def acquire_next_image(self):
    #    print(next(self.acquisition))
    
    #def acquire_in_loop(self):
        # start processes initialize ther run object
    #    try:
    #        self.expt_obj = ExptRun(acquisition=self.acquisition, save_dir=self.save_dir, params=deepcopy(self.params))
    #        self._ui.acquire_in_loop_button.setEnabled(False)
    #        print(f"Starting simulated acquisition: {self.simulated_acquisition}")
    #        #start_experiment(self.expt_obj, sim=self.simulated_acquisition)
    #       self.expt_obj.start(events=self.acquisition.events.copy(), sim=self.simulated_acquisition)
    #        print("Experiment run started .... ")
    #    except Exception as e:
    #        msg = QMessageBox()
    #        msg.setText(f"Experiment acquisition couldn't start due to: {e}")
    #        msg.setIcon(QMessageBox.Critical)
    #        msg.exec()

    #def stop_acquisition(self):
    #    if self.expt_obj is not None:
    #        self.expt_obj.stop()
    #    self._ui.acquire_in_loop_button.setEnabled(True)
    #    self.expt_obj = None
        

def run_ui():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    run_ui()

