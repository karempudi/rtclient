import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from rtclient.ui.qt_ui_classes.ui_main import Ui_MainWindow
from rtclient.ui.positions_window import PositionsWindow
from rtclient.ui.tweezer_window import TweezerWindow
from rtclient.ui.preview_window import PreviewWindow
from rtclient.microscope.acquisition import Acquisition
from rtclient.processes2 import ExptRun


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.positions_window = PositionsWindow()
        self.tweezer_window = TweezerWindow()
        self.preview_window = PreviewWindow()

        self.acquisition = None
        self.selected_values = None
        self.expt_obj = None
        self.simulated_acquisition = False

        self.setup_button_handlers()


    def setup_button_handlers(self):

        self._ui.positions_button.clicked.connect(self.show_positions_window)
        self._ui.rules_button.clicked.connect(self.show_positions_window)
        self._ui.preview_button.clicked.connect(self.show_preview_window)
        self.positions_window.send_events.connect(self.create_acquisition)

        self._ui.acquire_next_button.clicked.connect(self.acquire_next_image)

        self._ui.acquire_in_loop_button.clicked.connect(self.acquire_in_loop)

        self._ui.stop_button.clicked.connect(self.stop_acquisition)

        self._ui.tweezer_button.clicked.connect(self.show_tweezer_window)
    
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

    
    def closeEvent(self, event):
        self.tweezer_window.close()
        self.positions_window.close()
    
    def create_acquisition(self, selected_values):
        self.selected_values = selected_values
        #print("Events list recieved.. constructing acquisition object: ", len(selected_values['events']))
        self.acquisition = Acquisition(selected_values['events'])
        self.save_dir = selected_values['save_dir']
        self.simulated_acquisition = selected_values['simulated_acquisition']
        #print("Acquisition object set")
        print(f"Acquisition object set with {len(selected_values['events'])} events, simulated: {selected_values['simulated_acquisition']}")

    def acquire_next_image(self):
        print(next(self.acquisition))
    
    def acquire_in_loop(self):
        # start processes initialize ther run object
        try:
            self.expt_obj = ExptRun(acquisition=self.acquisition, save_dir=self.save_dir, save=False)
            self._ui.acquire_in_loop_button.setEnabled(False)
            print(f"Starting simulated acquisition: {self.simulated_acquisition}")
            #start_experiment(self.expt_obj, sim=self.simulated_acquisition)
            self.expt_obj.start(acquisition=self.acquisition, sim=self.simulated_acquisition)
            print("Experiment run started .... ")
        except Exception as e:
            msg = QMessageBox()
            msg.setText(f"Experiment acquisition couldn't start due to: {e}")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

    def stop_acquisition(self):
        if self.expt_obj is not None:
            self.expt_obj.stop()
        self._ui.acquire_in_loop_button.setEnabled(True)
        self.expt_obj = None
        

def run_ui():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    run_ui()

