import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from rtclient.ui.qt_ui_classes.ui_main import Ui_MainWindow
from rtclient.ui.positions_window import PositionsWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # button handlers
        self.setup_button_handlers()
        self.positions_window = PositionsWindow()
    
    def setup_button_handlers(self):

        self._ui.positions_button.clicked.connect(self.show_positions_window)
        self._ui.rules_button.clicked.connect(self.show_positions_window)
    
    @Slot()
    def show_positions_window(self):
        self.positions_window.show()
    
    def closeEvent(self, event):
        self.positions_window.close()
    


def run_ui():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    run_ui()

