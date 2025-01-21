import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from rtclient.ui.qt_ui_classes.ui_run import Ui_RunWindow

class RunWindow(QMainWindow):

    def __init__(self):
        super(RunWindow, self).__init__()
        self._ui = Ui_RunWindow()
        self._ui.setupUi(self)

        self.setup_button_handlers()

    def setup_button_handlers(self):
        pass

def run_ui():
    app = QApplication(sys.argv)
    window = RunWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    run_ui()