import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from rtclient.ui.qt_ui_classes.ui_run import Ui_RunWindow
from pathlib import Path
from rtseg.utils.param_io import load_params #type: ignore
import json
import time
from rtclient.processes3 import ExptRun, start_live_experiment

class RunWindow(QMainWindow):

    def __init__(self):
        super(RunWindow, self).__init__()
        self._ui = Ui_RunWindow()
        self._ui.setupUi(self)
        self.setWindowTitle("Expt runner ")

        self.setup_button_handlers()

        self.params = None
        self.events = None
        self.expt_obj = None

    def setup_button_handlers(self):
        self._ui.load_run_button.clicked.connect(self.load_expt_params)
        self._ui.start_run_button.clicked.connect(self.start_expt)
        self._ui.stop_run_button.clicked.connect(self.stop_expt)

    def load_expt_params(self):
        sys.stdout.write("Loadinng experimental parameters. Please select directory where events and params are stored.\n")
        sys.stdout.flush() 
        try:
            expt_save_dir = QFileDialog.getExistingDirectory(self, "Open Directory",
                '../', options=QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog)
            
            if expt_save_dir == '':
                msg = QMessageBox()
                msg.setText('Select directory where parameters are saved ...')
                msg.setIcon(QMessageBox.Critical)
                msg.exec()

            else:
                params_filename = Path(expt_save_dir) / Path('expt_params.yaml')
                events_filename = Path(expt_save_dir) / Path('events.json')

                print(expt_save_dir)
                print(params_filename)
                print(events_filename)
                self.params = load_params(params_filename, ref_type='expt')

                with open(events_filename) as f:
                    self.events = json.load(f)

                print('----- Loaded parameters ------')
                print(self.params)
                print('------------------------------')
                print('-------- Events --------------')
                print(self.events)
                print('------------------------------')
        except Exception as e:
            sys.stdout.write(f"Error in loading the experimental setup file -- {e}\n")
            sys.stdout.flush()
        
        finally:
            if self.params is not None:
                sys.stdout.write("Parameters for the experiment set from files \n")
                sys.stdout.flush()

    def start_expt(self):
        sys.stdout.write("Setting up experiment object from the parameters ...\n")
        sys.stdout.flush()

        if self.params is not None and self.events is not None:
            self.expt_obj = ExptRun(self.params, self.events)
            self._ui.start_run_button.setEnabled(False)
            self._ui.load_run_button.setEnabled(False)
            start_live_experiment(self.expt_obj, self.params.Save.sim)


    def stop_expt(self):
        sys.stdout.write("Stopping the experiment ...\n")
        sys.stdout.flush()

        # Stop the experiment and finally set it to None
        if self.expt_obj is not None:
            self.expt_obj.stop()

        time.sleep(3)
        self._ui.load_run_button.setEnabled(True)
        self._ui.start_run_button.setEnabled(True)
        self.expt_obj = None

    def closeEvent(self, event):
        sys.stdout.write("Closing and stopping the experiment ...\n")
        sys.stdout.flush()
        self.stop_expt()

def run_ui():
    app = QApplication(sys.argv)
    window = RunWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    run_ui()