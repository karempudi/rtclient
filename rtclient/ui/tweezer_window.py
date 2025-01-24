
import sys
import numpy as np
from PySide6.QtWidgets import QMainWindow
from rtclient.ui.qt_ui_classes.ui_tweezer import Ui_TweezerWindow

from PySide6.QtCore import Signal, QThread
from rtseg.utils.disk_ops import read_files

class DataFetchThread(QThread):

    data_fetched = Signal()

    def __init__(self, read_type, param, position, trap_no, max_imgs):
        super(DataFetchThread, self).__init__()
        self.read_type = read_type
        self.param = param
        self.position = position
        self.trap_no = trap_no
        self.max_imgs = max_imgs
        self.data = None

    def run(self):
        sys.stdout.write(f"Data fetching from Pos: {self.position} Trap no: {self.trap_no}\n")        
        sys.stdout.flush()

        try:
            image_data = read_files(self.read_type, self.param, self.position, self.trap_no, self.max_imgs)
            self.data = image_data
        except Exception as e:
            sys.stdout.write(f"Data couldn't be fetched due to {e}\n")
            sys.stdout.flush()
            self.data = {
                'image': np.random.normal(loc=0.0, scale=1.0, size=(100, 100)),
                'left_barcode': np.random.normal(loc=0.0, scale=1.0, size=(100, 10)),
                'right_barcode': np.random.normal(loc=0.0, scale=1.0, size=(100, 10))
            }
        finally:
            self.data_fetched.emit()

    def get_data(self):
        return self.data


class TweezerWindow(QMainWindow):

    def __init__(self, param=None):
        super(TweezerWindow, self).__init__()
        self._ui = Ui_TweezerWindow()
        self._ui.setupUi(self)

        self.setup_button_handlers()

        self.param = param

        self.current_pos = None
        self.current_trap_no = None
        self.position_no_validator = None
        self.trap_no_validator = None

        self.show_phase = True
        self.show_seg = False
        self.show_fluor = False
        self.show_dots_on_mask = False

        self.max_imgs = 20

        self.data_fetch_thread = None
        self.data_thread_running = False

    def setup_button_handlers(self):
        self._ui.image_plot.ui.histogram.hide()
        self._ui.image_plot.ui.roiBtn.hide()
        self._ui.image_plot.ui.menuBtn.hide()
        self._ui.barcode_plot_1.ui.histogram.hide()
        self._ui.barcode_plot_1.ui.roiBtn.hide()
        self._ui.barcode_plot_1.ui.menuBtn.hide()
        self._ui.barcode_plot_2.ui.histogram.hide()
        self._ui.barcode_plot_2.ui.roiBtn.hide()
        self._ui.barcode_plot_2.ui.menuBtn.hide()
        self._ui.fork_plots_all.ui.histogram.hide()
        self._ui.fork_plots_all.ui.roiBtn.hide()
        self._ui.fork_plots_all.ui.menuBtn.hide()
        self._ui.fork_plots_trap.ui.histogram.hide()
        self._ui.fork_plots_trap.ui.roiBtn.hide()
        self._ui.fork_plots_trap.ui.menuBtn.hide()


        self._ui.pos_no_edit.textChanged.connect(self.position_changed)
        self._ui.trap_no_edit.textChanged.connect(self.trap_changed)
        self._ui.fetch_button.clicked.connect(self.fetch_data)


        # set image kind to fetch
        self._ui.phase_image.toggled.connect(self.set_image_type)
        self._ui.cell_seg_image.toggled.connect(self.set_image_type) 
        self._ui.fluor_image.toggled.connect(self.set_image_type)
        self._ui.dots_on_mask_image.toggled.connect(self.set_image_type)

        # how many images to get
        self._ui.get_last20_radio.toggled.connect(self.set_no_images2get)
        self._ui.get_all_images_radio.toggled.connect(self.set_no_images2get)

    def set_params(self, param):
        self.param = param
        
    def position_changed(self):
        position = self._ui.pos_no_edit.text()
        try:
            int_pos = int(position)
        except Exception:
            self._ui.pos_no_edit.setText("")
            int_pos = None
        finally:
            self.current_pos = int_pos

        sys.stdout.write(f"Position set to {self.current_pos}\n")
        sys.stdout.flush()

    def trap_changed(self):
        trap_no = self._ui.trap_no_edit.text()
        try:
            int_trap_no = int(trap_no)
        except Exception:
            self._ui.trap_no_edit.setText("")
            int_trap_no = None
        finally:
            self.current_trap_no = int_trap_no
        sys.stdout.write(f"Trap no set to {self.current_trap_no}\n")
        sys.stdout.flush()

    def set_image_type(self):
        self.show_phase = self._ui.phase_image.isChecked()
        self.show_seg = self._ui.cell_seg_image.isChecked()
        self.show_fluor = self._ui.fluor_image.isChecked()
        self.show_dots_on_mask = self._ui.dots_on_mask_image.isChecked()

    def set_no_images2get(self):
        if self._ui.get_last20_radio.isChecked():
            self.max_imgs = 20
        else:
            self.max_imgs = None

    def fetch_data(self):
        if self.show_phase:
            read_type = 'phase'
        elif self.show_seg:
            read_type = 'cell_seg'
        elif self.show_fluor:
            read_type = 'fluor'
        elif self.show_dots_on_mask:
            read_type = 'dots_on_mask'
        
        if self.data_fetch_thread is None:
            self.data_fetch_thread = DataFetchThread(read_type, self.param, 
                        self.current_pos, self.current_trap_no, self.max_imgs)

            self.data_fetch_thread.start()
            self.data_fetch_thread.data_fetched.connect(self.update_image)


    def update_image(self):
        
        img_data = self.data_fetch_thread.get_data()

        if img_data is not None:
            self._ui.image_plot.setImage(img_data['image'].T, autoLevels=True, autoRange=False)
            self._ui.barcode_plot_1.setImage(img_data['left_barcode'].T, autoLevels=True, autoRange=True)
            self._ui.barcode_plot_2.setImage(img_data['right_barcode'].T, autoLevels=True, autoRange=True)
            sys.stdout.write("Image updated ....\n")
            sys.stdout.flush()

        self.data_fetch_thread.quit()
        self.data_fetch_thread.wait()
        self.data_fetch_thread = None

        return None
