import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from rtclient.ui.qt_ui_classes.ui_main import Ui_MainWindow
from rtclient.ui.positions_window import PositionsWindow
from rtclient.microscope.acquisition import Acquisition

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.positions_window = PositionsWindow()

        self.acquisition = None
        self.selected_values = None

        self.setup_button_handlers()

    def setup_button_handlers(self):

        self._ui.positions_button.clicked.connect(self.show_positions_window)
        self._ui.rules_button.clicked.connect(self.show_positions_window)
        self.positions_window.send_events.connect(self.create_acquisition)

        self._ui.acquire_next_button.clicked.connect(self.acquire_next_image)

        self._ui.acquire_in_loop_button.clicked.connect(self.acquire_in_loop)
    
    @Slot()
    def show_positions_window(self):
        self.positions_window.show()
    
    def closeEvent(self, event):
        self.positions_window.close()
    
    def create_acquisition(self, selected_values):
        self.selected_values = selected_values
        print("Events list recieved.. constructing acquisition object: ", len(selected_values['events']))
        self.acquisition = Acquisition(selected_values['events'])
        print("Acquisition object set")

    def acquire_next_image(self):
        print(next(self.acquisition))
    
    def acquire_in_loop(self):
        # start processes
        pass

def run_ui():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    run_ui()

