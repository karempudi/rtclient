import sys
import json
from pathlib import Path
from PySide6.QtCore import Slot
from PySide6.QtGui import QIntValidator, QValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QMessageBox, QFileDialog
from rtclient.ui.qt_ui_classes.ui_positions import Ui_PositionsWindow
from rtclient.utils.devices import check_mm_server_alive
from rtclient.microscope.utils import construct_pos_file, parse_positions_file
from pycromanager import Core # type: ignore
from rtclient.microscope.motion import RectGridMotion, TwoRectGridMotion 

RESOURES_PATH = Path(__file__).parent / Path('../resources/positions_dummies')
RESOURES_PATH = RESOURES_PATH.resolve()
DUMMY_POSTIONS_FILES = ("positions_20x_all.pos", "positions_20x_left.pos")

class PositionsWindow(QMainWindow):

    def __init__(self):
        super(PositionsWindow, self).__init__()
        self._ui = Ui_PositionsWindow()
        self._ui.setupUi(self)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        self.setWindowTitle("Positons and Rules generation")


        self.one_side = True
        self.enable_two_side_buttons(False)
        self.enable_one_side_buttons(True)
        self.corners_keys = {
            'first_half': ('TL1', 'TR1', 'BR1', 'BL1'),
            'second_half': ('TL2', 'TR2', 'BR2', 'BL2')
        }
        self.scope_devices = {
            'focus': 'PFSOffset',
            'XYStage': 'XYStage',
        }

        self.selected_values = {
            'n_sides': 1,
            'n_dummy_pos': None,
            'n_rows': 0,
            'n_cols': 0,
            'mm_version': 2.0,
            'orientation': 'horizontal',
            'marking_type': 'corners',
            'corners': {},
            'save_dir': None,
            'to_image' : [], # add group and preset configs
            'positions': [],
            'events': [],
            'selected_exposure': None,
            'selected_freq': None
        }

        self.group_dummies = {
            'imaging(dummy)': ['phase_fast', 'phase_slow', 
                        'phase_tweeze', 'venus']
        }

        self.setup_button_handlers()

    def setup_button_handlers(self):
        self._ui.one_rect_button.toggled.connect(self.set_layout_type)
        self._ui.two_rect_button.toggled.connect(self.set_layout_type)

        self._ui.corners_marking_button.clicked.connect(self.set_marking_type)
        self._ui.auto_marking_button.clicked.connect(self.set_marking_type)

        self._ui.dummy_positions_combo.currentTextChanged.connect(self.set_dummy_positions_type)

        self._ui.num_dummy_positions.setPlaceholderText("Numbers only 0-100")
        num_dummy_validator = QIntValidator(0, 99, self)
        self._ui.num_dummy_positions.setValidator(num_dummy_validator)
        self._ui.num_dummy_positions.textChanged.connect(self.set_num_dummy_positions)

        self._ui.chip_vertical_button.toggled.connect(self.set_chip_orientation)
        self._ui.chip_horizontal_button.toggled.connect(self.set_chip_orientation)

        self._ui.mm20_button.toggled.connect(self.set_mm_version)
        self._ui.mm14_button.toggled.connect(self.set_mm_version)

        self._ui.num_rows_edit.setPlaceholderText('Rows in one half 0-30')
        self._ui.num_cols_edit.setPlaceholderText('Cols in one half 0-30')
        rows_validator = QIntValidator(0, 30, self)
        cols_validator = QIntValidator(0, 30, self)
        self._ui.num_rows_edit.setValidator(rows_validator)
        self._ui.num_cols_edit.setValidator(cols_validator)
        self._ui.num_rows_edit.textChanged.connect(self.set_num_rows)
        self._ui.num_cols_edit.textChanged.connect(self.set_num_cols)


        self._ui.save_corners_button.clicked.connect(self.save_corners)
        self._ui.generate_positions_button.clicked.connect(self.generate_positions)
        self._ui.plot_path_button.clicked.connect(self.plot_path)

        self._ui.print_corners_button.clicked.connect(self.print_corners)
        self._ui.save_positions_button.clicked.connect(self.save_positions)

        # Marking positions
        self._ui.tl_button_1.clicked.connect(self.set_tl_1_position)
        self._ui.tr_button_1.clicked.connect(self.set_tr_1_position)
        self._ui.bl_button_1.clicked.connect(self.set_bl_1_position)
        self._ui.br_button_1.clicked.connect(self.set_br_1_position)

        self._ui.tl_button_2.clicked.connect(self.set_tl_2_position)
        self._ui.tr_button_2.clicked.connect(self.set_tr_2_position)
        self._ui.bl_button_2.clicked.connect(self.set_bl_2_position)
        self._ui.br_button_2.clicked.connect(self.set_br_2_position)

        # Test acquire
        self._ui.save_dir_button.clicked.connect(self.set_save_dir)
        self._ui.only_run_check.toggled.connect(self.set_run_type)


        # fill in the defaults for the presets and config groups
        self._ui.mm_groups_combo.clear()
        self._ui.mm_presets_combo.clear()
        if check_mm_server_alive():
            # add the groups and preset
            core = None
            try:
                core = Core()
                available_groups = core.get_available_config_groups()
                num_config_groups = available_groups.size()
                for i in range(num_config_groups):
                    config_name = available_groups.get(i)
                    self._ui.mm_groups_combo.insertItem(i, config_name)
            except Exception as e:
                msg = QMessageBox()
                msg.setText(f'Could not get groups from micromanger, check connection: {e}')
                msg.setIcon(QMessageBox.Critical)
                msg.exec()
            finally:
                if core:
                    del core
        else:
            for i, group_name in enumerate(self.group_dummies.keys()):
                self._ui.mm_groups_combo.insertItem(i, group_name)
        
        self._ui.mm_groups_combo.textActivated.connect(self.set_selected_group)

        # Imaging properties

        self._ui.exposure_edit.setPlaceholderText('1-300 (ms)')
        self._ui.imaging_freq_edit.setPlaceholderText('0-90 (mins)')
        exposure_validator = QIntValidator(0, 1000, self)
        imaging_freq_validator = QIntValidator(0, 90, self)
        self._ui.exposure_edit.setValidator(exposure_validator)
        self._ui.imaging_freq_edit.setValidator(imaging_freq_validator)
        self._ui.exposure_edit.textChanged.connect(self.set_exposure)
        self._ui.imaging_freq_edit.textChanged.connect(self.set_imaging_freq)


        self._ui.add_preset_button.clicked.connect(self.add_preset)
        self._ui.remove_preset_button.clicked.connect(self.remove_preset)


        # Event generation
        self._ui.generate_events_button.clicked.connect(self.generate_events)

        # Reset all to defaults states
        self._ui.reset_button.clicked.connect(self.reset_all)

        # Close window and set properties in higher windows
        self._ui.close_button.clicked.connect(self.close_window)


    
    @Slot()
    def set_layout_type(self, clicked):
        # image only one side or two sides, this will
        # effect the snaking pattern
        self.one_side = self._ui.one_rect_button.isChecked()
        self.two_sides = self._ui.two_rect_button.isChecked()
        if not self.one_side:
            self.enable_one_side_buttons(False)
            self.enable_two_side_buttons(True)
            self.selected_values['n_sides'] = 2
        else: 
            self.enable_two_side_buttons(False)
            self.enable_one_side_buttons(True)
            self.selected_values['n_sides'] = 1
        
        self.selected_values['corners'].clear()
        self.statusBar.showMessage(f"Imaging number of chip sides: {self.selected_values['n_sides']}", 1000)


    
    @Slot()
    def set_marking_type(self, clicked):
        marking_type = 'corners' if self._ui.corners_marking_button.isChecked() else 'auto'
        self.selected_values['marking_type'] = marking_type
        self.statusBar.showMessage(f"Postion marking type: {marking_type}", 1000) 

    @Slot()
    def set_dummy_positions_type(self, text):
        match text:
            case 'Follow boundary':
                pass

    @Slot()
    def set_num_dummy_positions(self):
        n_dummy_pos = self._ui.num_dummy_positions.text()
        state = self._ui.num_dummy_positions.validator().validate(n_dummy_pos, 0)
        match state[0]:
            case QValidator.Acceptable:
                color = '#c4df9b' # green
                self.selected_values['n_dummy_pos'] = int(state[1])
            case QValidator.Intermediate:
                color = '#fff79a' # yellow
                self.selected_values['n_dummy_pos'] = int(state[1]) if state[1] != '' else 0
            case QValidator.Invalid:
                color = '#f6989d' # red color
                self.selected_values['n_dummy_pos'] = None
        self._ui.num_dummy_positions.setStyleSheet('QLineEdit { background-color: %s }' % color)
        self.statusBar.showMessage(f"Number of dummy positions: {self.selected_values['n_dummy_pos']}", 1000)

    @Slot()
    def set_chip_orientation(self, clicked):
        orientation = 'horizontal' if self._ui.chip_horizontal_button.isChecked() else 'vertical'
        self.selected_values['orientation'] = orientation
        self.statusBar.showMessage(f'Chip orientation selected: {orientation}', 1000)

    @Slot()
    def set_mm_version(self, clicked):
        # set micromanager version to generate positon lists for
        mm_version = 2.0 if self._ui.mm20_button.isChecked() else 1.4
        self.selected_values['mm_version'] = mm_version
        self.statusBar.showMessage(f'MM version selected: {mm_version}', 1000)
    
    @Slot()
    def set_num_rows(self):
        n_rows = self._ui.num_rows_edit.text()
        state = self._ui.num_rows_edit.validator().validate(n_rows, 0)
        match state[0]:
            case QValidator.Acceptable:
                color = '#c4df9b' # green
                self.selected_values['n_rows'] = int(state[1])
            case QValidator.Intermediate:
                color = '#fff79a' # yellow
                self.selected_values['n_rows'] = int(state[1]) if state[1] != '' else 0
            case QValidator.Invalid:
                color = '#f6989d' # red color
                self.selected_values['n_rows'] = 0
        self._ui.num_rows_edit.setStyleSheet('QLineEdit { background-color: %s }' % color)
        self.statusBar.showMessage(f'Num of rows set to {n_rows}', 1000)

    
    @Slot()
    def set_num_cols(self):
        n_cols = self._ui.num_cols_edit.text()
        state = self._ui.num_cols_edit.validator().validate(n_cols, 0)
        match state[0]:
            case QValidator.Acceptable:
                color = '#c4df9b' # green
                self.selected_values['n_cols'] = int(state[1])
            case QValidator.Intermediate:
                color = '#fff79a' # yellow
                self.selected_values['n_cols'] = int(state[1]) if state[1] != '' else 0
            case QValidator.Invalid:
                color = '#f6989d' # red color
                self.selected_values['n_cols'] = 0
        self._ui.num_cols_edit.setStyleSheet('QLineEdit { background-color: %s }' % color)
        self.statusBar.showMessage(f'Num of columns set to {n_cols}', 1000)
   
    @Slot()
    def save_corners(self):
            
        write_json = None
        try:
            filename, _ = QFileDialog.getSaveFileName(self, "Save .pos positions file",
                            '.', "Position files (*.pos)", options=QFileDialog.DontUseNativeDialog)

            all_corners = []
            for corners_key in self.selected_values['corners']:
                all_corners.append(self.selected_values['corners'][corners_key])
            write_json = construct_pos_file(all_corners, 
                {'xy_device': self.scope_devices['XYStage'],
                'z_device': self.scope_devices['focus']}, version=self.selected_values['mm_version'])

            if filename == '' or write_json is None:
                raise FileNotFoundError('Filename not set correctly')
            filename = Path(filename)
            with open(filename, 'w') as fh:
                fh.write(json.dumps(write_json))

        except Exception as e:
            msg = QMessageBox()
            msg.setText(f'Saving corners positions failed due to {e}')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

    @Slot()
    def generate_positions(self):
        chip_orientation = self.selected_values['orientation']
        sides = self.selected_values['n_sides']
        nrows = self.selected_values['n_rows']
        ncols = self.selected_values['n_cols']
        if sides == 2:
            motion_object = TwoRectGridMotion(chip_orientation=chip_orientation) 
        else:
            motion_object = RectGridMotion(movement_type='top') if chip_orientation == 'vertical' else RectGridMotion(movement_type='left')
        
        motion_object.set_rows(nrows)
        motion_object.set_cols(ncols)
        
        motion_object.construct_grid()
        self.selected_values['positions'] = motion_object.positions

    @Slot()
    def plot_path(self):
        pass
    
    @Slot()
    def print_corners(self):
        print(self.selected_values['corners'])
    
    @Slot()
    def save_positions(self):
        pass

    def set_positon_and_label(self, label):
        if check_mm_server_alive():
            position_dict = self.get_mm_current_position(label)
            self.selected_values['corners'][label] = position_dict
            self.statusBar.showMessage(f"{label} position grabbed from micromanager ...", 1000)
        else:
            
            # load dummies if there is no micromanager connection
            if self.selected_values['n_sides'] == 1:
                dummy_filename = RESOURES_PATH / Path(DUMMY_POSTIONS_FILES[1])
            else:
                dummy_filename = RESOURES_PATH / Path(DUMMY_POSTIONS_FILES[0])

            self.statusBar.showMessage(f'Setting dummy position for position: {label}')
            _, corner_positions = parse_positions_file(dummy_filename,
                                positions_type='corners')
            for position in corner_positions:
                if position['label'] == 'Pos' + label:
                    self.selected_values['corners'][label] = position
            self.statusBar.showMessage(f'Setting dummy position for position: {label}')

    def get_mm_current_position(self, label):
        core = None
        position_dict = None
        try:
            if not check_mm_server_alive():
                raise ValueError('Could not connect to micromanager')
            core = Core()
            if core.get_focus_device() != self.scope_devices['focus']:
                raise ValueError('Focus device is not PFSOffset')
            if core.get_xy_stage_device != self.scope_devices['XYStage']:
                raise ValueError('XY stage device is not XYStage')

            x = core.get_x_position()
            y = core.get_y_position()
            z = core.get_auto_focus_offset()
            position_dict = {
                'x': x,
                'y': y,
                'z': z,
                'grid_row': 0,
                'grid_col': 0,
                'label': 'Pos' + label,
            }
        except Exception as e:
            msg = QMessageBox()
            msg.setText(f'Could not grad position {label} from micromanger, check connection: {e}')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
        finally:
            if core:
                del core
            self.statusBar.showMessage(f"Positon {label} set to {position_dict}")
            return position_dict

    @Slot()
    def set_tl_1_position(self):
        self.set_positon_and_label('TL1')
    
    @Slot()
    def set_tr_1_position(self):
        self.set_positon_and_label('TR1')
    
    @Slot()
    def set_bl_1_position(self):
        self.set_positon_and_label('BL1')
    
    @Slot()
    def set_br_1_position(self):
        self.set_positon_and_label('BR1')
     
    @Slot()
    def set_tl_2_position(self):
        self.set_positon_and_label('TL2')
    
    @Slot()
    def set_tr_2_position(self):
        self.set_positon_and_label('TR2')
    
    @Slot()
    def set_bl_2_position(self):
        self.set_positon_and_label('BL2')
    
    @Slot()
    def set_br_2_position(self):
        self.set_positon_and_label('BR2')


    @Slot()
    def enable_one_side_buttons(self, value):
        self._ui.tl_button_1.setEnabled(value)
        self._ui.tr_button_1.setEnabled(value)
        self._ui.bl_button_1.setEnabled(value)
        self._ui.br_button_1.setEnabled(value)
    
    @Slot()
    def enable_two_side_buttons(self, value):
        self._ui.tl_button_1.setEnabled(value)
        self._ui.tr_button_1.setEnabled(value)
        self._ui.bl_button_1.setEnabled(value)
        self._ui.br_button_1.setEnabled(value)
        self._ui.tl_button_2.setEnabled(value)
        self._ui.tr_button_2.setEnabled(value)
        self._ui.bl_button_2.setEnabled(value)
        self._ui.br_button_2.setEnabled(value)

    @Slot()
    def set_save_dir(self):
        pass
    
    @Slot()
    def set_run_type(self):
        pass

    @Slot()
    def set_selected_group(self, text):
        # update with available presets
        core = None
        self._ui.mm_presets_combo.clear()
        if check_mm_server_alive():
            try:
                core = Core()
                # get presets for the current text group name selected
                available_presets = core.get_available_configs(text)
                num_presets_in_group = available_presets.size()
                for i in range(num_presets_in_group):
                    preset = available_presets.get(i)
                    self._ui.mm_presets_combo.insertItem(i, preset)
            except Exception as e:
                msg = QMessageBox()
                msg.setText(f'Could not grad presets from micromanger, check connection: {e}')
                msg.setIcon(QMessageBox.Critical)
                msg.exec()
            finally:
                if core:
                    del core
        else:
            if text in self.group_dummies:
                for i, preset in enumerate(self.group_dummies[text]):
                    self._ui.mm_presets_combo.insertItem(i, preset)
    
    @Slot()
    def set_exposure(self):
        exposure_time = self._ui.exposure_edit.text()
        state = self._ui.exposure_edit.validator().validate(exposure_time, 0)
        valid = False
        match state[0]:
            case QValidator.Acceptable:
                color = '#c4df9b' # green
                valid = True
            case QValidator.Intermediate:
                color = '#fff79a' # yellow
                valid = False
            case QValidator.Invalid:
                color = '#f6989d' # red color
                valid = False
        self._ui.exposure_edit.setStyleSheet('QLineEdit { background-color: %s }' % color)
        self.statusBar.showMessage(f'Exposure set to {state[1]}', 1000)
        self.selected_values['selected_exposure'] = int(state[1]) if valid else None

    
    @Slot()
    def set_imaging_freq(self):
        imaging_freq = self._ui.imaging_freq_edit.text()
        state = self._ui.imaging_freq_edit.validator().validate(imaging_freq, 0)
        valid = False
        match state[0]:
            case QValidator.Acceptable:
                color = '#c4df9b' # green
                valid = True
            case QValidator.Intermediate:
                color = '#fff79a' # yellow
                valid = False
            case QValidator.Invalid:
                color = '#f6989d' # red color
                valid = False
        self._ui.imaging_freq_edit.setStyleSheet('QLineEdit { background-color: %s }' % color)
        self.statusBar.showMessage(f'Imaging freq set to {state[1]}', 1000)
        self.selected_values['selected_freq'] = int(state[1]) if valid else None

    @Slot()
    def add_preset(self):
        # get current selected group and selected preset
        # add it to the imaging rules
        # current group
        current_group = self._ui.mm_groups_combo.currentText()
        # current preset
        current_preset = self._ui.mm_presets_combo.currentText()

        current_exposure_time = self.selected_values['selected_exposure']
        current_imaging_freq = self.selected_values['selected_freq']

        self._ui.show_imaging_list.addItem(str(current_group) + ','
                                        + str(current_preset) + ','
                                        + str(current_exposure_time) + ','
                                        + str(current_imaging_freq))
        self.selected_values['to_image'].append((current_group, current_preset, 
                                            current_exposure_time, current_imaging_freq))
    
    @Slot()
    def remove_preset(self):
        # remove selected imaging type
        selected_items = self._ui.show_imaging_list.selectedItems()
        for item in selected_items:
            group, preset, exposure, freq = tuple(item.text().split(','))
            self._ui.show_imaging_list.takeItem(self._ui.show_imaging_list.row(item))
            # remove the imaging from the to_image 
            freq = int(freq) if freq != 'None' else None
            exposure = int(exposure) if exposure != 'None' else None
            self.selected_values['to_image'].remove((group, preset, exposure, freq))
    
    @Slot()
    def generate_events(self):
        pass

    @Slot()
    def reset_all(self):
        pass

    @Slot()
    def close_window(self):
        self.close()


def run_window():
    app = QApplication(sys.argv)
    window = PositionsWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run_window()