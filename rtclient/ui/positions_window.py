import sys
from PySide6.QtCore import Slot
from PySide6.QtGui import QIntValidator, QValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar
from rtclient.ui.qt_ui_classes.ui_positions import Ui_PositionsWindow
from rtclient.utils.devices import check_mm_server_alive


class PositionsWindow(QMainWindow):

    def __init__(self):
        super(PositionsWindow, self).__init__()
        self._ui = Ui_PositionsWindow()
        self._ui.setupUi(self)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        self.setWindowTitle("Positons and Rules generation")

        self.setup_button_handlers()

        self.selected_values = {
            'n_dummy_pos': None,
            'n_rows': 0,
            'n_cols': 0,
        }
        # check platform and fill values
        if check_mm_server_alive():
            self.selected_values['TL1'] = {}
            self.selected_values['TR1'] = {}
            self.selected_values['BR1'] = {}
            self.selected_values['BL1'] = {}
            self.selected_values['BR2'] = {}
            self.selected_values['BL2'] = {}
            self.selected_values['TR2'] = {}
            self.selected_values['TL2'] = {}
        else:
            # Read and fill dummy values on linux or any test system
            pass

            



    def setup_button_handlers(self):
        self._ui.one_rect_button.toggled.connect(self.set_layout_type)
        self._ui.two_rect_button.toggled.connect(self.set_layout_type)

        self._ui.pattern_type_combo.currentTextChanged.connect(self.set_corner_selection_type)

        self._ui.dummy_positions_combo.currentTextChanged.connect(self.set_dummy_positions_type)

        self._ui.num_dummy_positions.setPlaceholderText("Numbers only 0-100")
        num_dummy_validator = QIntValidator(0, 100, self)
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

    
    @Slot()
    def set_layout_type(self, clicked):
        # image only one side or two sides, this will
        # effect the snaking pattern
        self.one_side = self._ui.one_rect_button.isChecked()
        self.two_sides = self._ui.two_rect_button.isChecked()

    
    @Slot()
    def set_corner_selection_type(self, text):
        pass
    
    @Slot()
    def set_dummy_positions_type(self, text):
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

    @Slot()
    def set_chip_orientation(self, clicked):
        pass

    @Slot()
    def set_mm_version(self, clicked):
        # set micromanager version to generate positon lists for
        pass
    
    @Slot()
    def set_num_rows(self):
        pass
    
    @Slot()
    def set_num_cols(self):
        pass
    
    @Slot()
    def save_positions(self):
        pass

    @Slot()
    def update_path_plot(self):
        pass

    def set_positon_and_label(self, label):
        self.statusBar.showMessage(f"{label} position selected ..", 2000)
        #position_dict = self.get_mm_current_position()

    def get_mm_current_position(self):
        pass
        
    
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
        self._ui.tl_button.setEnabled(value)
        self._ui.tr_button.setEnabled(value)
        self._ui.bl_button.setEnabled(value)
        self._ui.br_button.setEnabled(value)
    
    @Slot()
    def enable_two_side_buttons(self, value):
        self._ui.tl_button.setEnabled(value)
        self._ui.tr_button.setEnabled(value)
        self._ui.bl_button.setEnabled(value)
        self._ui.br_button.setEnabled(value)
        self._ui.tl_button_2.setEnabled(value)
        self._ui.tr_button_2.setEnabled(value)
        self._ui.bl_button_2.setEnabled(value)
        self._ui.br_button_2.setEnabled(value)


def run_window():
    app = QApplication(sys.argv)
    window = PositionsWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run_window()