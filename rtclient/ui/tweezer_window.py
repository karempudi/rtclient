
from PySide6.QtWidgets import QMainWindow
from rtclient.ui.qt_ui_classes.ui_tweezer import Ui_TweezerWindow

class TweezerWindow(QMainWindow):

    def __init__(self):
        super(TweezerWindow, self).__init__()
        self._ui = Ui_TweezerWindow()
        self._ui.setupUi(self)
