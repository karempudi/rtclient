
import sys
import numpy as np
from PySide6.QtWidgets import QMainWindow, QMessageBox, QListWidget
from rtclient.ui.qt_ui_classes.ui_tweezer import Ui_TweezerWindow
from matplotlib.backends.backend_qtagg import FigureCanvas, NavigationToolbar2QT #type: ignore
from matplotlib.figure import Figure
from PySide6.QtCore import Signal, QThread
from rtseg.utils.disk_ops import read_files
import pyqtgraph as pg
from matplotlib import cm
from pathlib import Path
import rtseg.cells.scoring as sco
from rtseg.utils.get_fork_init import read_all_fork_data_around_init
from rtseg.cells.scoring import score_all_fork_plots, score_plotter
from os.path import exists
import h5py
import libpysal
import matplotlib.pyplot as plt

def mpl_cmap_to_pg_colormap(cmap_name):
    cmap = cm.get_cmap(cmap_name)
    colors = cmap(np.linspace(0.0, 1.0, 256))
    colors = [pg.mkColor(int(r*255), int(g*255), int(b*255)) for r, g, b, _ in colors]
    positions = np.linspace(0, 1, 256)
    return pg.ColorMap(positions, colors)

class DataFetchThread(QThread):

    data_fetched = Signal()

    def __init__(self, read_type, param, position, trap_no, trap_no_disp, max_imgs):
        super(DataFetchThread, self).__init__()
        self.read_type = read_type
        self.param = param
        self.position = position
        self.trap_no = trap_no
        self.trap_no_disp = trap_no_disp
        self.max_imgs = max_imgs
        self.data = None

    def run(self):
        sys.stdout.write(f"Data fetching from Pos: {self.position} Trap no: {self.trap_no_disp}\n")        
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

class AllForkFetchThread(QThread):

    fork_fetched = Signal()

    def __init__(self, read_type, param, position, trap_no, trap_no_disp):
        super(AllForkFetchThread, self).__init__()
        self.read_type = read_type
        self.param = param
        self.position = position
        self.trap_no = trap_no
        self.trap_no_disp = trap_no_disp
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

class SingleForkFetchThread(QThread):

    fork_fetched = Signal()

    def __init__(self, read_type, param, position, trap_no, trap_no_disp):
        super(SingleForkFetchThread, self).__init__()
        self.read_type = read_type
        self.param = param
        self.position = position
        self.trap_no = trap_no
        self.trap_no_disp = trap_no_disp
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

class PreComputeForkScoreFetchThread(QThread):

    fork_fetched = Signal()

    def __init__(self, param):
        super(PreComputeForkScoreFetchThread, self).__init__()
        self.param = param
        self.fork_data = None
        self.all_scores = None
        self.scores_median_mad = None

    def run(self):
        try:
            file_dir_hdf5 = Path(self.param.Save.directory) / Path('fork_score_data.h5')
            if not exists(file_dir_hdf5):
                self.fork_data, moran_weights = read_all_fork_data_around_init(self.param)
                self.all_scores, self.scores_median_mad = score_all_fork_plots(self.fork_data, moran_weights)
                self.save_data_to_file()
            else:
                self.fork_data, self.all_scores, self.scores_median_mad = self.load_data()
        except Exception as e:
            sys.stdout.write(f"Fork plot data fetching failed due to {e}")
            sys.stdout.flush()
            self.fork_data = {}
            self.all_scores = {}
            self.scores_median_mad = {}
        finally:
            self.fork_fetched.emit()

    def save_data_to_file(self):

        save_dir = Path(self.param.Save.directory)
        with h5py.File(save_dir / 'fork_score_data.h5', 'w') as hdf:

            fork_group = hdf.create_group('fork_data')
            for key, value in self.fork_data.items():
                fork_group.create_dataset(key, data=value)

            score_group = hdf.create_group('all_scores')
            for key, value in self.all_scores.items():
                score_group.create_dataset(key, data=value)

            median_mad_group = hdf.create_group('scores_median_mad')
            for key, value in self.scores_median_mad.items():
                median_mad_group.create_dataset(key, data=value)                    

    def get_data(self):
        return self.fork_data, self.all_scores, self.scores_median_mad
    
    def load_data(self):
        file_dir_hdf5 = Path(self.param.Save.directory) / Path('fork_score_data.h5')
    
        with h5py.File(file_dir_hdf5, 'r') as hdf:
            self.fork_data = {}
            for key in hdf['fork_data'].keys():
                self.fork_data[key] = hdf['fork_data'][key][()]

            self.all_scores = {}
            for key in hdf['all_scores'].keys():
                self.all_scores[key] = hdf['all_scores'][key][()]
            
            self.scores_median_mad = {}
            for key in hdf['scores_median_mad'].keys():
                self.scores_median_mad[key] = hdf['scores_median_mad'][key][()]

        sys.stdout.write("Loaded precomputed fork data from file\n")
        sys.stdout.flush()

        return self.fork_data, self.all_scores, self.scores_median_mad

class TweezerWindow(QMainWindow):

    def __init__(self, param=None):
        super(TweezerWindow, self).__init__()
        self._ui = Ui_TweezerWindow()
        self._ui.setupUi(self)

        self.setup_button_handlers()

        self.param = param

        self.current_pos = None
        self.current_trap_no = None
        self.current_trap_no_disp = None
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

        self.abins_init = None
        self.lbins_init = None
        self.abins_init_inds = None 
        self.lbins_init_inds = None
        self.init_area = None 
        self.full_heatmap_init = None
        self.area_plot_extent = None 
        self.color_lims = None
        self.flat_full_heatmap_init = None
        self.moran_weight = None
        self.e_dists = None

        self.all_scores = None
        self.scores_median_mad = None

        self.fork_type = None
        self.single_fork_fetch_thread = None
        self.all_fork_fetch_thread = None
        self.precomputed_fork_thread = None
        self.single_fork_thread_running = False
        self.all_fork_thread_running = False
        
        self.selected_pos = None
        self.selected_trap_no = None
        self.show_active_or_tweeze = 'acitve' # will use to toggle between 'active' and 'tweeze'
        self.active_traps_list = []
        self.tweeze_traps_list = []


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



        # populate the active list
        self._ui.get_traps_button.clicked.connect(self.get_all_traps_list)
        self._ui.reset_button.clicked.connect(self.reset_lists)

        # Viewer list of positions trap wise (active and tweeze positions lists)
        self._ui.active_traps_list.setSortingEnabled(True)
        self._ui.active_traps_list.setSelectionMode(QListWidget.SingleSelection)
        self._ui.tweeze_traps_list.setSortingEnabled(True)
        self._ui.tweeze_traps_list.setSelectionMode(QListWidget.SingleSelection)
        self._ui.active_traps_list.itemSelectionChanged.connect(self.show_selected_active_trap)
        self._ui.tweeze_traps_list.itemSelectionChanged.connect(self.show_selected_tweeze_trap)

        self._ui.to_tweeze_list_button.clicked.connect(self.send_trap_to_tweeze_list)
        self._ui.to_active_list_button.clicked.connect(self.send_trap_to_active_list)

        self._ui.precompute_forks_button.clicked.connect(self.precompute_forks_and_score)

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
            self.current_trap_no = int_trap_no - 1
        except Exception:
            self._ui.trap_no_edit.setText("")
            int_trap_no = None
        finally:
            self.current_trap_no_disp = int_trap_no 

        sys.stdout.write(f"Trap no set to {self.current_trap_no_disp}\n")
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

    def precompute_forks_and_score(self, clicked):
        sys.stdout.write("Pre-computing forks for scoring\n")
        sys.stdout.flush()

        if self.precomputed_fork_thread is None:
            self.precomputed_fork_thread = PreComputeForkScoreFetchThread(self.param)
            self.precomputed_fork_thread.start()
            self.precomputed_fork_thread.fork_fetched.connect(self.precomputed_fork_data_scores_init)
            
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
                        self.current_pos, self.current_trap_no, 
                        self.current_trap_no_disp, self.max_imgs)

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
        sys.stdout.write(f"Getting single trap forks for Pos: {self.current_pos} Trap: {self.current_trap_no_disp}\n")
        sys.stdout.flush()

        self.fork_type = 'single'
        if self.single_fork_fetch_thread is None:
            self.single_fork_fetch_thread = SingleForkFetchThread('single_trap_data_forks', self.param, 
                        self.current_pos, self.current_trap_no, self.current_trap_no_disp)

            self.single_fork_fetch_thread.start()
            self.single_fork_fetch_thread.fork_fetched.connect(self.update_forks_image)

    def update_all_data_forks(self):
        sys.stdout.write("Getting all data forks ...\n")
        sys.stdout.flush()

        self.fork_type = 'all'

        if self.all_fork_fetch_thread is None:
            self.all_fork_fetch_thread = AllForkFetchThread('all_forks', self.param, 
                        self.current_pos, self.current_trap_no, self.current_trap_no_disp)

            self.all_fork_fetch_thread.start()
            self.all_fork_fetch_thread.fork_fetched.connect(self.update_forks_image)

    def precomputed_fork_data_scores_init(self):
        # The _ is fork_data, currently not using it, and it is only sliced fork plots
        _, self.all_scores, self.scores_median_mad = self.precomputed_fork_thread.get_data()

        self.precomputed_fork_thread.quit()
        self.precomputed_fork_thread.wait()
        self.precomputed_fork_thread = None

    def plot_scores(self):
        #Hook this to a button
        
        if self.all_scores is None and self.scores_median_mad is None:
            sys.stdout.write(f"Fork plots were not pre-computed or not loaded into memory. Doing that now.\n")
            sys.stdout.flush()
            self.precompute_forks_and_score()

            
        tot_nr_traps = self.all_scores['correlation'].flatten().size
        plot_range = np.arange(1, tot_nr_traps+1, 1)
        x_fill = np.array([1, tot_nr_traps, tot_nr_traps, 1])
        
        score_plotter(self.all_scores['correlation'], self.scores_median_mad['correlation'], 
                    plot_range, x_fill, 'Pearson correlation coefficient')

        score_plotter(self.all_scores['ssim'], self.scores_median_mad['ssim'], 
                    plot_range, x_fill, 'SSIM')
        
        score_plotter(self.all_scores['moran'][0], self.scores_median_mad['moran'][0], 
                    plot_range, x_fill, 'Cross-Moran\'s I')

        score_plotter(self.all_scores['ks'][0], self.scores_median_mad['ks'][0], 
                    plot_range, x_fill, 'Kolmogorov-Smirnov results')

        score_plotter(self.all_scores['sobolevs'], self.scores_median_mad['sobolevs'], 
                    plot_range, x_fill, 'Sobolev norm')

        score_plotter(self.all_scores['energies'], self.scores_median_mad['energies'], 
                    plot_range, x_fill, 'Energy test')
        
        print('Plotting')
       

    
    def update_forks_image(self):
        
        if self.fork_type == 'all':
            fork_data = self.all_fork_fetch_thread.get_data()
        elif self.fork_type == 'single':
            fork_data = self.single_fork_fetch_thread.get_data()

        if fork_data is not None:
            if self.fork_type == 'all':
                (x, y) = fork_data['extent']
                self.all_forks_axes.clear()
                #Commenting out the full fork plot code for now, but it can be added back in if needed 
                
                plot_heatmap = self.all_forks_axes.matshow(fork_data['heatmap'], aspect='auto', interpolation='none', 
                                extent=[x[0], x[-1], y[-1], y[0]], origin='upper', cmap='jet')
                self.all_forks_axes.plot(-0.5 * fork_data['mean_cell_lengths'], y, 'w', linewidth=2)
                self.all_forks_axes.plot(+0.5 * fork_data['mean_cell_lengths'],y, 'w', linewidth=2)
                self.all_forks_axes.axhline(fork_data['init_area'], color='red', linestyle='--', linewidth=2)
                self.all_forks_axes.set_xlabel('Cell long axis (µm)')
                self.all_forks_axes.set_ylabel('Cell size (µm$^2$)')
                self.all_forks_axes.set_xlim(-3, 3)
                self.all_forks_axes.set_ylim(3, y[0])
                
             
                #Around initiation fork plot 
                lbins_around_init = fork_data['lbins_around_init']
                area_bins_around_init = fork_data['area_bins_around_init']
                abins_inds_around_init = fork_data['abins_inds_around_init']
                #self.all_forks_axes.matshow(fork_data['heatmap_around_init'], aspect='auto', interpolation='none',
                #                            extent=[lbins_around_init[0], lbins_around_init[-1], area_bins_around_init[-1], area_bins_around_init[0]], origin='upper', cmap='jet')
                #self.all_forks_axes.plot(-0.5 * fork_data['mean_cell_lengths_around_init'], y[abins_inds_around_init[0:-1]], 'w', linewidth=2)
                #self.all_forks_axes.plot(+0.5 * fork_data['mean_cell_lengths_around_init'], y[abins_inds_around_init[0:-1]], 'w', linewidth=2)
                #self.all_forks_axes.axhline(fork_data['init_area'], color='red', linestyle='--', linewidth=2)
                self.all_forks_view.draw()

                self.abins_init = area_bins_around_init
                self.lbins_init = lbins_around_init
                self.abins_init_inds = abins_inds_around_init
                self.lbins_init_inds = fork_data['lbins_inds_around_init'] 
                self.init_area = fork_data['init_area']
                self.full_heatmap_init = fork_data['heatmap_around_init']
                self.plot_extent = fork_data['extent']
                self.color_lims = (plot_heatmap.norm.vmin, plot_heatmap.norm.vmax)
                self.flat_full_heatmap_init = fork_data['flat_heatmap_init']
                self.moran_weight = fork_data['moran_weight']
                self.e_dists = fork_data['e_dists']

                sys.stdout.write("Updated fork data for all positions ...\n")
                sys.stdout.flush()


            elif self.fork_type == 'single':
                (x, y) = self.plot_extent

                heatmap_trap = fork_data['heatmap_trap']
                mean_cell_lengths_trap = fork_data['mean_cell_lengths_trap']
                #heatmap_trap_init = heatmap_trap[np.ix_(self.abins_init_inds, self.lbins_init_inds)]
                #mean_cell_lengths_trap_init = mean_cell_lengths_trap[self.abins_init_inds[0:-1]]

                self.single_fork_axes.clear()

                #Full fork plot for a single trap
                self.single_fork_axes.matshow(heatmap_trap, aspect='auto', interpolation='none', 
                                              extent=[x[0], x[-1], y[-1], y[0]], origin='upper', cmap='jet', 
                                              vmin=self.color_lims[0], vmax=self.color_lims[1])
                self.single_fork_axes.plot(-0.5 * mean_cell_lengths_trap, y, 'w', linewidth=2)
                self.single_fork_axes.plot(+0.5 * mean_cell_lengths_trap, y, 'w', linewidth=2)
                self.single_fork_axes.axhline(self.init_area, color='red', linestyle='--', linewidth=2)
                self.single_fork_axes.set_xlabel('Cell long axis (µm)')
                self.single_fork_axes.set_ylabel('Cell size (µm$^2$)')
                self.single_fork_axes.set_xlim(-3, 3)
                self.single_fork_axes.set_ylim(3, y[0])
                


                #Cropped single trap fork plot and scoring 
                heatmap_trap_init = sco.crop_single_trap_fork_plot(heatmap_trap, self.abins_init_inds, self.lbins_init_inds)
                flat_heatmap_trap_init = heatmap_trap_init.flatten()

                corrcoeff = sco.score_correlation_coefficient(self.flat_full_heatmap_init, flat_heatmap_trap_init)
                ssim_score = sco.score_ssim(self.flat_full_heatmap_init, flat_heatmap_trap_init)
                cross_moran_I, moran_pval, moran_z_score = sco.score_cross_moran(self.flat_full_heatmap_init, flat_heatmap_trap_init, self.moran_weight)
                ks_score, ks_pval = sco.score_kolmogorov_smirnov(self.flat_full_heatmap_init, flat_heatmap_trap_init)
                sobolev_norm = sco.score_sobolev_norm(self.full_heatmap_init, heatmap_trap_init)
                enery_score = sco.score_energy_test(self.flat_full_heatmap_init, flat_heatmap_trap_init, self.e_dists)



                #Fork plot around initiation for a single trap
                #self.single_fork_axes.matshow(heatmap_trap_init, aspect='auto', interpolation='none',
                 #           extent=[self.lbins_init[0], self.lbins_init[-1], self.abins_init[-1], self.abins_init[0]], origin='upper', cmap='jet')
                #self.single_fork_axes.plot(-0.5 * mean_cell_lengths_trap_init, self.area_plot_extent[self.abins_init_inds[0:-1]], 'w', linewidth=2)
                #self.single_fork_axes.plot(+0.5 * mean_cell_lengths_trap_init, self.area_plot_extent[self.abins_init_inds[0:-1]], 'w', linewidth=2)
                #self.single_fork_axes.set_xlabel('Cell long axis (µm)')
                #self.single_fork_axes.set_ylabel('Cell size (µm^2)')
                #self.single_fork_axes.axhline(self.init_area, color='red', linestyle='--', linewidth=2)

                self.single_fork_view.draw()

                sys.stdout.write(f"Updated fork data  for Pos: {self.current_pos} trap no: {self.current_trap_no_disp}\n")
                sys.stdout.write(f"Correlation coefficient: {corrcoeff}\n SSIM: {ssim_score}\n Cross-Moran I: {cross_moran_I}\n KS-score: {ks_score}\n Sobolev norm: {sobolev_norm}\n Energy test score:{enery_score}\n")
                sys.stdout.flush()

        if self.fork_type == 'all':
            self.all_fork_fetch_thread.quit()
            self.all_fork_fetch_thread.wait()
            self.all_fork_fetch_thread = None
        elif self.fork_type == 'single':
            self.single_fork_fetch_thread.quit()
            self.single_fork_fetch_thread.wait()
            self.single_fork_fetch_thread = None
 

        return None


    def get_all_traps_list(self, clicked):

        # Populate all the traps in the active list
        self.active_traps_list.clear()
        self.tweeze_traps_list.clear()

        try:

            # get traps
            save_dir  = Path(self.param.Save.directory)

            # get all position directories
            position_dirs = sorted(list(save_dir.glob('Pos*')))
            num_traps = self.param.BarcodeAndChannels.num_blocks_per_image * self.param.BarcodeAndChannels.num_traps_per_block

            for directory in position_dirs:
                pos = int(directory.name[3:])
                for trap_no in range(1, num_traps+1):
                    self.active_traps_list.append((pos, trap_no))
                    item = 'Pos: ' + str(pos) + ' Trap: ' + str(trap_no)
                    self._ui.active_traps_list.addItem(item)

        except Exception as e:
            msg = QMessageBox()
            msg.setText(f'Unable to fetch traps list due to: {e}')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()

    def reset_lists(self, clicked):
        self.active_traps_list.clear()
        self.tweeze_traps_list.clear()
        self._ui.active_traps_list.clear()
        self._ui.tweeze_traps_list.clear()

    def show_selected_tweeze_trap(self):

        # clear selection so that the highlight goes away in the active traps list
        self._ui.active_traps_list.clearSelection()
        # what is selected 
        selected_items = self._ui.tweeze_traps_list.selectedItems()

        # only one item # a bit weird. but ok. works
        position = None
        trap_no = None
        for item in selected_items:
            item_text = item.text()
            position = int(item_text.split(" ")[1])
            trap_no = int(item_text.split(" ")[3])
            sys.stdout.write(f"Getting tweeze single trap forks for Pos: {position} Trap: {trap_no}\n")
            sys.stdout.flush()

        self.fork_type = 'single'
        if self.single_fork_fetch_thread is None and (position is not None and trap_no is not None):
            self.single_fork_fetch_thread = SingleForkFetchThread('single_trap_data_forks', self.param, 
                        position, trap_no-1, trap_no)

            self.single_fork_fetch_thread.start()
            self.single_fork_fetch_thread.fork_fetched.connect(self.update_forks_image)


         
    def show_selected_active_trap(self):
        # clear selection so that the highlight goes away in the tweeze traps list
        self._ui.tweeze_traps_list.clearSelection()
        # what is selected 
        selected_items = self._ui.active_traps_list.selectedItems()

        # only one item # a bit weird. but ok. works
        position = None
        trap_no = None
        for item in selected_items:
            item_text = item.text()
            position = int(item_text.split(" ")[1])
            trap_no = int(item_text.split(" ")[3])
            sys.stdout.write(f"Getting active single trap forks for Pos: {position} Trap: {trap_no}\n")
            sys.stdout.flush()
    
        self.fork_type = 'single'
        if self.single_fork_fetch_thread is None and (position is not None and trap_no is not None):
            self.single_fork_fetch_thread = SingleForkFetchThread('single_trap_data_forks', self.param, 
                        position, trap_no-1, trap_no)

            self.single_fork_fetch_thread.start()
            self.single_fork_fetch_thread.fork_fetched.connect(self.update_forks_image)



    def send_trap_to_tweeze_list(self, clicked):
        try:
            selected_items = self._ui.active_traps_list.selectedItems()
            for item in selected_items:
                self._ui.active_traps_list.takeItem(self._ui.active_traps_list.row(item))
                item_text = item.text()
                position = int(item_text.split(" ")[1])
                trap_no = int(item_text.split(" ")[3])
                self._ui.tweeze_traps_list.addItem(item_text)
                self.active_traps_list.remove((position, trap_no))
                self.tweeze_traps_list.append((position, trap_no))
                sys.stdout.write(f"Moved Pos: {position}  Trap: {trap_no} to tweeze list\n")
                sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(f"Moving trap to tweeeze list failed due to {e}\n")
            sys.stdout.flush()
    
    def send_trap_to_active_list(self, clicked):
        try:
            selected_items = self._ui.tweeze_traps_list.selectedItems()
            for item in selected_items:
                self._ui.tweeze_traps_list.takeItem(self._ui.tweeze_traps_list.row(item))
                item_text = item.text()
                position = int(item_text.split(" ")[1])
                trap_no = int(item_text.split(" ")[3])
                self._ui.active_traps_list.addItem(item_text)
                self.tweeze_traps_list.remove((position, trap_no))
                self.active_traps_list.append((position, trap_no))
                sys.stdout.write(f"Moved Pos: {position}  Trap: {trap_no} to active list\n")
                sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(f"Moving trap to active list failed due to {e}\n")
            sys.stdout.flush()
            
        

