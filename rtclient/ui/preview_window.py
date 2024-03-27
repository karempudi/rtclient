
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow
from rtclient.ui.qt_ui_classes.ui_preview import Ui_PreviewWindow


class PreviewWindow(QMainWindow):

    def __init__(self):
        super(PreviewWindow, self).__init__()
        self._ui = Ui_PreviewWindow()
        self._ui.setupUi(self)

        self.setup_button_handlers()
    
    def setup_button_handlers(self):
        self._ui.close_button.clicked.connect(self.close_window)
        self._ui.save_button.clicked.connect(self.save_acquisition)

    @Slot()
    def close_window(self):
        self.close()

    @Slot()
    def save_acquisition(self):
        pass