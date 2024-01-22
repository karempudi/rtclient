import sys
from PySide6.QtCore import Slot
from PySide6.QtGui import QIntValidator, QValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QMessageBox
from rtclient.ui.qt_ui_classes.ui_positions import Ui_PositionsWindow
from rtclient.utils.devices import check_mm_server_alive
#from rtclient.microscope.utils import parse_positions_file
from pycromanager import Core # type: ignore

class PositionsWindow(QMainWindow):

    def __init__(self):
        super(PositionsWindow, self).__init__()
        self._ui = Ui_PositionsWindow()
        self._ui.setupUi(self)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        self.setWindowTitle("Positons and Rules generation")

        self.setup_button_handlers()

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
        }
        # check platform and fill values
        if check_mm_server_alive():
            pass
        else:
            # Read and fill dummy values on linux or any test system
            pass


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


        self._ui.save_positions_button.clicked.connect(self.save_positions)

        self._ui.update_path_button.clicked.connect(self.update_path_plot)

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


        # Imaging properties

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
        mm_version = '2.0' if self._ui.mm20_button.isChecked() else '1.4'
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
    def save_positions(self):
        pass

    @Slot()
    def update_path_plot(self):
        pass

    def set_positon_and_label(self, label):
        self.statusBar.showMessage(f"{label} position selected ..", 1000)
        position_dict = self.get_mm_current_position(label)
        self.selected_values['corners'][label] = position_dict

    def get_mm_current_position(self, label):
        core = None
        position_dict = None
        try:
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
    def add_preset(self):
        pass
    
    @Slot()
    def remove_preset(self):
        pass
    
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