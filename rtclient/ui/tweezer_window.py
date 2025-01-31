
import sys
import numpy as np
from PySide6.QtWidgets import QMainWindow
from rtclient.ui.qt_ui_classes.ui_tweezer import Ui_TweezerWindow
from matplotlib.backends.backend_qtagg import FigureCanvas, NavigationToolbar2QT #type: ignore
from matplotlib.figure import Figure
from PySide6.QtCore import Signal, QThread
from rtseg.utils.disk_ops import read_files
import pyqtgraph as pg
from matplotlib import cm

def mpl_cmap_to_pg_colormap(cmap_name):
    cmap = cm.get_cmap(cmap_name)
    colors = cmap(np.linspace(0.0, 1.0, 256))
    colors = [pg.mkColor(int(r*255), int(g*255), int(b*255)) for r, g, b, _ in colors]
    positions = np.linspace(0, 1, 256)
    return pg.ColorMap(positions, colors)

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

class ForkFetchThread(QThread):

    fork_fetched = Signal()

    def __init__(self, read_type, param, position, trap_no):
        super(ForkFetchThread, self).__init__()
        self.read_type = read_type
        self.param = param
        self.position = position
        self.trap_no = trap_no
        self.fork_data = None

    def run(self):
        try:
            self.fork_data = read_files(self.read_type, self.param, self.position, self.trap_no)
        except Exception as e:
            sys.stdout.write(f"Fork plot data fetching failed due to {e}")
            sys.stdout.flush()
            self.fork_data = {
                'heatmap': np.random.normal(loc=0.0, scale=1.0, size=(100, 100)),
                'mean_cell_lengths': np.random.normal(loc=0.0, scale=1.0, size=(100,)),
                'extent': (None, None)
            }
        finally:
            self.fork_fetched.emit()
    
    def get_data(self):
        return self.fork_data

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
        self.read_type = None

        self.max_imgs = 20

        self.data_fetch_thread = None
        self.data_thread_running = False



        self.fork_type = None
        self.fork_fetch_thread = None
        self.fork_thread_running = False


    def setup_button_handlers(self):

        self.image_view = FigureCanvas(Figure(figsize=(8, 12)))
        self.image_axes = self.image_view.figure.subplots()
        self.image_toolbar = NavigationToolbar2QT(self.image_view, self)
        self._ui.image_layout.addWidget(self.image_toolbar)
        self._ui.image_layout.addWidget(self.image_view)


        self.barcode_left_view = FigureCanvas(Figure(figsize=(8, 3)))
        self.barcode_left_axes = self.barcode_left_view.figure.subplots()
        self._ui.barcode_left_layout.addWidget(self.barcode_left_view)

        self.barcode_right_view = FigureCanvas(Figure(figsize=(8, 3)))
        self.barcode_right_axes = self.barcode_right_view.figure.subplots()
        self._ui.barcode_right_layout.addWidget(self.barcode_right_view)


        self.single_fork_view = FigureCanvas(Figure(figsize=(5,3)))
        self.single_fork_axes = self.single_fork_view.figure.subplots()
        self.single_fork_toolbar = NavigationToolbar2QT(self.single_fork_view, self)
        self._ui.single_trap_fork_layout.addWidget(self.single_fork_toolbar)
        self._ui.single_trap_fork_layout.addWidget(self.single_fork_view)


        self.all_forks_view = FigureCanvas(Figure(figsize=(5, 3)))
        self.all_forks_axes = self.all_forks_view.figure.subplots()
        self.all_forks_toolbar = NavigationToolbar2QT(self.all_forks_view, self)
        self._ui.all_data_fork_layout.addWidget(self.all_forks_toolbar)
        self._ui.all_data_fork_layout.addWidget(self.all_forks_view)



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
        

        # fork plotting buttons
        self._ui.current_trap_forks_button.clicked.connect(self.update_single_trap_forks)
        self._ui.all_data_forks_button.clicked.connect(self.update_all_data_forks)

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
            read_type = 'segmented_cells_by_trap'
        elif self.show_fluor:
            read_type = 'fluor'
        elif self.show_dots_on_mask:
            read_type = 'dots_on_mask'

        self.read_type = read_type

        if self.data_fetch_thread is None:
            self.data_fetch_thread = DataFetchThread(read_type, self.param, 
                        self.current_pos, self.current_trap_no, self.max_imgs)

            self.data_fetch_thread.start()
            self.data_fetch_thread.data_fetched.connect(self.update_image)


    def update_image(self):
        
        img_data = self.data_fetch_thread.get_data()

        if img_data is not None:
            # based on image type and data retrieved plot the image

            if self.read_type == 'phase':
                self.image_axes.clear()
                self.image_axes.imshow(img_data['image'], cmap='gray')
                self.image_view.draw()

                self.barcode_left_axes.clear()
                self.barcode_left_axes.imshow(img_data['left_barcode'], cmap='gray')
                self.barcode_left_view.draw()

                self.barcode_right_axes.clear()
                self.barcode_right_axes.imshow(img_data['right_barcode'], cmap='gray')
                self.barcode_right_view.draw()

            elif self.read_type == 'segmented_cells_by_trap':
                self.image_axes.clear()
                self.image_axes.imshow(img_data['image'], cmap='viridis')
                self.image_view.draw()


                self.barcode_left_axes.clear()
                self.barcode_left_axes.imshow(img_data['left_barcode'], cmap='gray')
                self.barcode_left_view.draw()

                self.barcode_right_axes.clear()
                self.barcode_right_axes.imshow(img_data['right_barcode'], cmap='gray')
                self.barcode_right_view.draw()


            elif self.read_type == 'fluor':
                self.image_axes.clear()
                self.image_axes.imshow(img_data['image'], cmap='gray')


                # plot dot coordinates
                self.image_axes.plot(img_data['dots'][:, 1], img_data['dots'][:, 0], 'ro')

                self.image_view.draw()

                self.barcode_left_axes.clear()
                self.barcode_left_axes.imshow(img_data['left_barcode'], cmap='gray') 
                self.barcode_left_view.draw()

                self.barcode_right_axes.clear()
                self.barcode_right_axes.imshow(img_data['right_barcode'], cmap='gray')
                self.barcode_right_view.draw()


            elif self.read_type == 'dots_on_mask':
                self.image_axes.clear()
                self.image_axes.imshow(img_data['image'], cmap='viridis')
                self.image_axes.plot(img_data['dots'][:, 1], img_data['dots'][:, 0], 'ro')
                self.image_view.draw()

                # plot dot coordinates

                self.barcode_left_axes.clear()
                self.barcode_left_axes.imshow(img_data['left_barcode'], cmap='gray')
                self.barcode_left_view.draw()

                self.barcode_right_axes.clear()
                self.barcode_right_axes.imshow(img_data['right_barcode'], cmap='gray')
                self.barcode_right_view.draw()


            sys.stdout.write("Image updated ....\n")
            sys.stdout.flush()

        self.data_fetch_thread.quit()
        self.data_fetch_thread.wait()
        self.data_fetch_thread = None

        return None

    def update_single_trap_forks(self):
        sys.stdout.write(f"Getting single trap forks for Pos: {self.current_pos} Trap: {self.current_trap_no}\n")
        sys.stdout.flush()

        self.fork_type = 'single'
        if self.fork_fetch_thread is None:
            self.fork_fetch_thread = ForkFetchThread('single_trap_data_forks', self.param, 
                        self.current_pos, self.current_trap_no)

            self.fork_fetch_thread.start()
            self.fork_fetch_thread.fork_fetched.connect(self.update_forks_image)

    def update_all_data_forks(self):
        sys.stdout.write("Getting all data forks ...\n")
        sys.stdout.flush()

        self.fork_type = 'all'

        if self.fork_fetch_thread is None:
            self.fork_fetch_thread = ForkFetchThread('all_forks', self.param, 
                        self.current_pos, self.current_trap_no)

            self.fork_fetch_thread.start()
            self.fork_fetch_thread.fork_fetched.connect(self.update_forks_image)

    def update_forks_image(self):
        
        fork_data = self.fork_fetch_thread.get_data()

        if fork_data is not None:
            if self.fork_type == 'all':
                (x, y) = fork_data['extent']
                self.all_forks_axes.clear()
                self.all_forks_axes.matshow(fork_data['heatmap'], aspect='auto', interpolation='none', 
                                extent=[x[0], x[-1], y[-1], y[0]], origin='upper')
                self.all_forks_axes.plot(-0.5 * fork_data['mean_cell_lengths'], y, 'w', linewidth=2)
                self.all_forks_axes.plot(+0.5 * fork_data['mean_cell_lengths'],y, 'w', linewidth=2)
                self.all_forks_axes.set_xlabel('Cell long axis (µm)')
                self.all_forks_axes.set_ylabel('Cell size (µm^2)')

                self.all_forks_view.draw()

            elif self.fork_type == 'single':
                (x, y) = fork_data['extent']
                self.single_fork_axes.clear()
                self.single_fork_axes.imshow(fork_data['heatmap'], aspect='auto', interpolation='none',
                                extent=[x[0], x[-1], y[-1], y[0]], origin='upper')
                self.single_fork_axes.plot(-0.5 * fork_data['mean_cell_lengths'], y, 'w', linewidth=2)
                self.single_fork_axes.plot(+0.5 * fork_data['mean_cell_lengths'], y, 'w', linewidth=2)
                self.single_fork_axes.set_xlabel('Cell long axis (µm)')
                self.single_fork_axes.set_ylabel('Cell size (µm^2)')

                self.single_fork_view.draw()

        self.fork_fetch_thread.quit()
        self.fork_fetch_thread.wait()
        self.fork_fetch_thread = None

        return None





            
        

