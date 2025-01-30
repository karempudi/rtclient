# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'positions.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_PositionsWindow(object):
    def setupUi(self, PositionsWindow):
        if not PositionsWindow.objectName():
            PositionsWindow.setObjectName(u"PositionsWindow")
        PositionsWindow.resize(1182, 787)
        self.centralwidget = QWidget(PositionsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.positions_group = QGroupBox(self.centralwidget)
        self.positions_group.setObjectName(u"positions_group")
        self.positions_group.setGeometry(QRect(10, 10, 441, 411))
        self.formLayoutWidget = QWidget(self.positions_group)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 30, 401, 244))
        self.positions_layout = QFormLayout(self.formLayoutWidget)
        self.positions_layout.setObjectName(u"positions_layout")
        self.positions_layout.setContentsMargins(0, 0, 0, 0)
        self.num_sides_label = QLabel(self.formLayoutWidget)
        self.num_sides_label.setObjectName(u"num_sides_label")

        self.positions_layout.setWidget(0, QFormLayout.LabelRole, self.num_sides_label)

        self.grid_type_layout = QHBoxLayout()
        self.grid_type_layout.setObjectName(u"grid_type_layout")
        self.one_rect_button = QRadioButton(self.formLayoutWidget)
        self.sidesGroup = QButtonGroup(PositionsWindow)
        self.sidesGroup.setObjectName(u"sidesGroup")
        self.sidesGroup.addButton(self.one_rect_button)
        self.one_rect_button.setObjectName(u"one_rect_button")
        self.one_rect_button.setChecked(True)

        self.grid_type_layout.addWidget(self.one_rect_button)

        self.two_rect_button = QRadioButton(self.formLayoutWidget)
        self.sidesGroup.addButton(self.two_rect_button)
        self.two_rect_button.setObjectName(u"two_rect_button")
        self.two_rect_button.setAutoExclusive(True)

        self.grid_type_layout.addWidget(self.two_rect_button)


        self.positions_layout.setLayout(0, QFormLayout.FieldRole, self.grid_type_layout)

        self.making_patterns_label = QLabel(self.formLayoutWidget)
        self.making_patterns_label.setObjectName(u"making_patterns_label")

        self.positions_layout.setWidget(1, QFormLayout.LabelRole, self.making_patterns_label)

        self.dummy_positions_label = QLabel(self.formLayoutWidget)
        self.dummy_positions_label.setObjectName(u"dummy_positions_label")

        self.positions_layout.setWidget(2, QFormLayout.LabelRole, self.dummy_positions_label)

        self.dummy_positions_combo = QComboBox(self.formLayoutWidget)
        self.dummy_positions_combo.addItem("")
        self.dummy_positions_combo.addItem("")
        self.dummy_positions_combo.addItem("")
        self.dummy_positions_combo.setObjectName(u"dummy_positions_combo")

        self.positions_layout.setWidget(2, QFormLayout.FieldRole, self.dummy_positions_combo)

        self.num_dummy_positions_label = QLabel(self.formLayoutWidget)
        self.num_dummy_positions_label.setObjectName(u"num_dummy_positions_label")
        self.num_dummy_positions_label.setEnabled(False)

        self.positions_layout.setWidget(3, QFormLayout.LabelRole, self.num_dummy_positions_label)

        self.num_dummy_positions = QLineEdit(self.formLayoutWidget)
        self.num_dummy_positions.setObjectName(u"num_dummy_positions")
        self.num_dummy_positions.setEnabled(False)

        self.positions_layout.setWidget(3, QFormLayout.FieldRole, self.num_dummy_positions)

        self.chip_orientation_label = QLabel(self.formLayoutWidget)
        self.chip_orientation_label.setObjectName(u"chip_orientation_label")

        self.positions_layout.setWidget(4, QFormLayout.LabelRole, self.chip_orientation_label)

        self.chip_orientation_layout = QHBoxLayout()
        self.chip_orientation_layout.setObjectName(u"chip_orientation_layout")
        self.chip_horizontal_button = QRadioButton(self.formLayoutWidget)
        self.orientationGroup = QButtonGroup(PositionsWindow)
        self.orientationGroup.setObjectName(u"orientationGroup")
        self.orientationGroup.addButton(self.chip_horizontal_button)
        self.chip_horizontal_button.setObjectName(u"chip_horizontal_button")
        self.chip_horizontal_button.setChecked(True)

        self.chip_orientation_layout.addWidget(self.chip_horizontal_button)

        self.chip_vertical_button = QRadioButton(self.formLayoutWidget)
        self.orientationGroup.addButton(self.chip_vertical_button)
        self.chip_vertical_button.setObjectName(u"chip_vertical_button")
        self.chip_vertical_button.setChecked(False)

        self.chip_orientation_layout.addWidget(self.chip_vertical_button)


        self.positions_layout.setLayout(4, QFormLayout.FieldRole, self.chip_orientation_layout)

        self.mm_version_label = QLabel(self.formLayoutWidget)
        self.mm_version_label.setObjectName(u"mm_version_label")

        self.positions_layout.setWidget(5, QFormLayout.LabelRole, self.mm_version_label)

        self.mm_version_layout = QHBoxLayout()
        self.mm_version_layout.setObjectName(u"mm_version_layout")
        self.mm20_button = QRadioButton(self.formLayoutWidget)
        self.versionGroup = QButtonGroup(PositionsWindow)
        self.versionGroup.setObjectName(u"versionGroup")
        self.versionGroup.addButton(self.mm20_button)
        self.mm20_button.setObjectName(u"mm20_button")
        self.mm20_button.setChecked(True)

        self.mm_version_layout.addWidget(self.mm20_button)

        self.mm14_button = QRadioButton(self.formLayoutWidget)
        self.versionGroup.addButton(self.mm14_button)
        self.mm14_button.setObjectName(u"mm14_button")

        self.mm_version_layout.addWidget(self.mm14_button)


        self.positions_layout.setLayout(5, QFormLayout.FieldRole, self.mm_version_layout)

        self.num_rows_label = QLabel(self.formLayoutWidget)
        self.num_rows_label.setObjectName(u"num_rows_label")

        self.positions_layout.setWidget(6, QFormLayout.LabelRole, self.num_rows_label)

        self.num_rows_edit = QLineEdit(self.formLayoutWidget)
        self.num_rows_edit.setObjectName(u"num_rows_edit")

        self.positions_layout.setWidget(6, QFormLayout.FieldRole, self.num_rows_edit)

        self.num_cols_label = QLabel(self.formLayoutWidget)
        self.num_cols_label.setObjectName(u"num_cols_label")

        self.positions_layout.setWidget(7, QFormLayout.LabelRole, self.num_cols_label)

        self.num_cols_edit = QLineEdit(self.formLayoutWidget)
        self.num_cols_edit.setObjectName(u"num_cols_edit")

        self.positions_layout.setWidget(7, QFormLayout.FieldRole, self.num_cols_edit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.corners_marking_button = QRadioButton(self.formLayoutWidget)
        self.markingGroup = QButtonGroup(PositionsWindow)
        self.markingGroup.setObjectName(u"markingGroup")
        self.markingGroup.addButton(self.corners_marking_button)
        self.corners_marking_button.setObjectName(u"corners_marking_button")
        self.corners_marking_button.setChecked(True)

        self.horizontalLayout_2.addWidget(self.corners_marking_button)

        self.auto_marking_button = QRadioButton(self.formLayoutWidget)
        self.markingGroup.addButton(self.auto_marking_button)
        self.auto_marking_button.setObjectName(u"auto_marking_button")
        self.auto_marking_button.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.auto_marking_button)


        self.positions_layout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayoutWidget = QWidget(self.positions_group)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 280, 401, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.save_corners_button = QPushButton(self.horizontalLayoutWidget)
        self.save_corners_button.setObjectName(u"save_corners_button")

        self.horizontalLayout_3.addWidget(self.save_corners_button)

        self.generate_positions_button = QPushButton(self.horizontalLayoutWidget)
        self.generate_positions_button.setObjectName(u"generate_positions_button")

        self.horizontalLayout_3.addWidget(self.generate_positions_button)

        self.plot_path_button = QPushButton(self.horizontalLayoutWidget)
        self.plot_path_button.setObjectName(u"plot_path_button")

        self.horizontalLayout_3.addWidget(self.plot_path_button)

        self.horizontalLayoutWidget_4 = QWidget(self.positions_group)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 330, 401, 27))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.print_corners_button = QPushButton(self.horizontalLayoutWidget_4)
        self.print_corners_button.setObjectName(u"print_corners_button")

        self.horizontalLayout_4.addWidget(self.print_corners_button)

        self.reload_positions_button = QPushButton(self.horizontalLayoutWidget_4)
        self.reload_positions_button.setObjectName(u"reload_positions_button")
        self.reload_positions_button.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.reload_positions_button)

        self.save_positions_button = QPushButton(self.horizontalLayoutWidget_4)
        self.save_positions_button.setObjectName(u"save_positions_button")

        self.horizontalLayout_4.addWidget(self.save_positions_button)

        self.horizontalLayoutWidget_5 = QWidget(self.positions_group)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 370, 419, 27))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.generate_dummy_button = QPushButton(self.horizontalLayoutWidget_5)
        self.generate_dummy_button.setObjectName(u"generate_dummy_button")

        self.horizontalLayout_5.addWidget(self.generate_dummy_button)

        self.save_dummy_button = QPushButton(self.horizontalLayoutWidget_5)
        self.save_dummy_button.setObjectName(u"save_dummy_button")

        self.horizontalLayout_5.addWidget(self.save_dummy_button)

        self.plot_dummy_button = QPushButton(self.horizontalLayoutWidget_5)
        self.plot_dummy_button.setObjectName(u"plot_dummy_button")

        self.horizontalLayout_5.addWidget(self.plot_dummy_button)

        self.rules_group = QGroupBox(self.centralwidget)
        self.rules_group.setObjectName(u"rules_group")
        self.rules_group.setGeometry(QRect(460, 10, 371, 261))
        self.formLayoutWidget_2 = QWidget(self.rules_group)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 120, 226, 121))
        self.rules_form_layout = QFormLayout(self.formLayoutWidget_2)
        self.rules_form_layout.setObjectName(u"rules_form_layout")
        self.rules_form_layout.setContentsMargins(0, 0, 0, 0)
        self.mm_groups_label = QLabel(self.formLayoutWidget_2)
        self.mm_groups_label.setObjectName(u"mm_groups_label")

        self.rules_form_layout.setWidget(0, QFormLayout.LabelRole, self.mm_groups_label)

        self.mm_preset_label = QLabel(self.formLayoutWidget_2)
        self.mm_preset_label.setObjectName(u"mm_preset_label")

        self.rules_form_layout.setWidget(1, QFormLayout.LabelRole, self.mm_preset_label)

        self.exposure_label = QLabel(self.formLayoutWidget_2)
        self.exposure_label.setObjectName(u"exposure_label")

        self.rules_form_layout.setWidget(2, QFormLayout.LabelRole, self.exposure_label)

        self.exposure_edit = QLineEdit(self.formLayoutWidget_2)
        self.exposure_edit.setObjectName(u"exposure_edit")

        self.rules_form_layout.setWidget(2, QFormLayout.FieldRole, self.exposure_edit)

        self.mm_groups_combo = QComboBox(self.formLayoutWidget_2)
        self.mm_groups_combo.setObjectName(u"mm_groups_combo")

        self.rules_form_layout.setWidget(0, QFormLayout.FieldRole, self.mm_groups_combo)

        self.mm_presets_combo = QComboBox(self.formLayoutWidget_2)
        self.mm_presets_combo.setObjectName(u"mm_presets_combo")

        self.rules_form_layout.setWidget(1, QFormLayout.FieldRole, self.mm_presets_combo)

        self.imaging_freq_label = QLabel(self.formLayoutWidget_2)
        self.imaging_freq_label.setObjectName(u"imaging_freq_label")

        self.rules_form_layout.setWidget(3, QFormLayout.LabelRole, self.imaging_freq_label)

        self.imaging_freq_edit = QLineEdit(self.formLayoutWidget_2)
        self.imaging_freq_edit.setObjectName(u"imaging_freq_edit")

        self.rules_form_layout.setWidget(3, QFormLayout.FieldRole, self.imaging_freq_edit)

        self.show_imaging_list = QListWidget(self.rules_group)
        self.show_imaging_list.setObjectName(u"show_imaging_list")
        self.show_imaging_list.setGeometry(QRect(10, 30, 241, 81))
        self.add_preset_button = QPushButton(self.rules_group)
        self.add_preset_button.setObjectName(u"add_preset_button")
        self.add_preset_button.setGeometry(QRect(260, 30, 89, 25))
        self.remove_preset_button = QPushButton(self.rules_group)
        self.remove_preset_button.setObjectName(u"remove_preset_button")
        self.remove_preset_button.setGeometry(QRect(260, 60, 89, 25))
        self.test_acquire_group = QGroupBox(self.centralwidget)
        self.test_acquire_group.setObjectName(u"test_acquire_group")
        self.test_acquire_group.setGeometry(QRect(270, 430, 231, 221))
        self.horizontalLayoutWidget_2 = QWidget(self.test_acquire_group)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 120, 228, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dont_save_data = QCheckBox(self.horizontalLayoutWidget_2)
        self.dont_save_data.setObjectName(u"dont_save_data")

        self.horizontalLayout.addWidget(self.dont_save_data)

        self.horizontalLayoutWidget_6 = QWidget(self.test_acquire_group)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 170, 240, 25))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.simulated_acquisition_check = QCheckBox(self.horizontalLayoutWidget_6)
        self.simulated_acquisition_check.setObjectName(u"simulated_acquisition_check")

        self.horizontalLayout_6.addWidget(self.simulated_acquisition_check)

        self.verticalLayoutWidget_2 = QWidget(self.test_acquire_group)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 30, 201, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.save_dir_button = QPushButton(self.verticalLayoutWidget_2)
        self.save_dir_button.setObjectName(u"save_dir_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_dir_button.sizePolicy().hasHeightForWidth())
        self.save_dir_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.save_dir_button)

        self.save_dir_path_display = QLineEdit(self.verticalLayoutWidget_2)
        self.save_dir_path_display.setObjectName(u"save_dir_path_display")
        self.save_dir_path_display.setReadOnly(True)

        self.verticalLayout.addWidget(self.save_dir_path_display)

        self.mark_positions_group = QGroupBox(self.centralwidget)
        self.mark_positions_group.setObjectName(u"mark_positions_group")
        self.mark_positions_group.setGeometry(QRect(10, 430, 251, 221))
        self.gridLayoutWidget = QWidget(self.mark_positions_group)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 232, 171))
        self.choose_positions_layout = QGridLayout(self.gridLayoutWidget)
        self.choose_positions_layout.setObjectName(u"choose_positions_layout")
        self.choose_positions_layout.setContentsMargins(0, 0, 0, 0)
        self.bl_button_1 = QPushButton(self.gridLayoutWidget)
        self.bl_button_1.setObjectName(u"bl_button_1")

        self.choose_positions_layout.addWidget(self.bl_button_1, 3, 0, 1, 1)

        self.tl_button_1 = QPushButton(self.gridLayoutWidget)
        self.tl_button_1.setObjectName(u"tl_button_1")

        self.choose_positions_layout.addWidget(self.tl_button_1, 1, 0, 1, 1)

        self.tr_button_1 = QPushButton(self.gridLayoutWidget)
        self.tr_button_1.setObjectName(u"tr_button_1")

        self.choose_positions_layout.addWidget(self.tr_button_1, 2, 0, 1, 1)

        self.br_button_1 = QPushButton(self.gridLayoutWidget)
        self.br_button_1.setObjectName(u"br_button_1")

        self.choose_positions_layout.addWidget(self.br_button_1, 4, 0, 1, 1)

        self.tl_button_2 = QPushButton(self.gridLayoutWidget)
        self.tl_button_2.setObjectName(u"tl_button_2")

        self.choose_positions_layout.addWidget(self.tl_button_2, 1, 1, 1, 1)

        self.tr_button_2 = QPushButton(self.gridLayoutWidget)
        self.tr_button_2.setObjectName(u"tr_button_2")

        self.choose_positions_layout.addWidget(self.tr_button_2, 2, 1, 1, 1)

        self.bl_button_2 = QPushButton(self.gridLayoutWidget)
        self.bl_button_2.setObjectName(u"bl_button_2")

        self.choose_positions_layout.addWidget(self.bl_button_2, 3, 1, 1, 1)

        self.br_button_2 = QPushButton(self.gridLayoutWidget)
        self.br_button_2.setObjectName(u"br_button_2")

        self.choose_positions_layout.addWidget(self.br_button_2, 4, 1, 1, 1)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(470, 290, 380, 51))
        self.reset_close_layout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.reset_close_layout.setObjectName(u"reset_close_layout")
        self.reset_close_layout.setContentsMargins(0, 0, 0, 0)
        self.generate_events_button = QPushButton(self.horizontalLayoutWidget_3)
        self.generate_events_button.setObjectName(u"generate_events_button")

        self.reset_close_layout.addWidget(self.generate_events_button)

        self.preview_events_button = QPushButton(self.horizontalLayoutWidget_3)
        self.preview_events_button.setObjectName(u"preview_events_button")

        self.reset_close_layout.addWidget(self.preview_events_button)

        self.reset_button = QPushButton(self.horizontalLayoutWidget_3)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setEnabled(False)

        self.reset_close_layout.addWidget(self.reset_button)

        self.close_button = QPushButton(self.horizontalLayoutWidget_3)
        self.close_button.setObjectName(u"close_button")

        self.reset_close_layout.addWidget(self.close_button)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(510, 380, 351, 271))
        self.matplotlib_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.matplotlib_layout.setObjectName(u"matplotlib_layout")
        self.matplotlib_layout.setContentsMargins(0, 0, 0, 0)
        self.preview_list = QListWidget(self.centralwidget)
        self.preview_list.setObjectName(u"preview_list")
        self.preview_list.setGeometry(QRect(870, 30, 301, 621))
        PositionsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PositionsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1182, 21))
        PositionsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PositionsWindow)
        self.statusbar.setObjectName(u"statusbar")
        PositionsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PositionsWindow)

        QMetaObject.connectSlotsByName(PositionsWindow)
    # setupUi

    def retranslateUi(self, PositionsWindow):
        PositionsWindow.setWindowTitle(QCoreApplication.translate("PositionsWindow", u"MainWindow", None))
        self.positions_group.setTitle(QCoreApplication.translate("PositionsWindow", u"Positon layout", None))
        self.num_sides_label.setText(QCoreApplication.translate("PositionsWindow", u"No of sides", None))
        self.one_rect_button.setText(QCoreApplication.translate("PositionsWindow", u"One Side", None))
        self.two_rect_button.setText(QCoreApplication.translate("PositionsWindow", u"Two sides", None))
        self.making_patterns_label.setText(QCoreApplication.translate("PositionsWindow", u"Marking patterns", None))
        self.dummy_positions_label.setText(QCoreApplication.translate("PositionsWindow", u"Dummy", None))
        self.dummy_positions_combo.setItemText(0, QCoreApplication.translate("PositionsWindow", u"None", None))
        self.dummy_positions_combo.setItemText(1, QCoreApplication.translate("PositionsWindow", u"Follow boundary", None))
        self.dummy_positions_combo.setItemText(2, QCoreApplication.translate("PositionsWindow", u"Fastest way", None))

        self.num_dummy_positions_label.setText(QCoreApplication.translate("PositionsWindow", u"No of dummy  positions", None))
        self.chip_orientation_label.setText(QCoreApplication.translate("PositionsWindow", u"Chip orientation", None))
        self.chip_horizontal_button.setText(QCoreApplication.translate("PositionsWindow", u"horizontal", None))
        self.chip_vertical_button.setText(QCoreApplication.translate("PositionsWindow", u"vertical", None))
        self.mm_version_label.setText(QCoreApplication.translate("PositionsWindow", u"Micromanager Version", None))
        self.mm20_button.setText(QCoreApplication.translate("PositionsWindow", u"2.0", None))
        self.mm14_button.setText(QCoreApplication.translate("PositionsWindow", u"1.4", None))
        self.num_rows_label.setText(QCoreApplication.translate("PositionsWindow", u"Number of rows", None))
        self.num_cols_label.setText(QCoreApplication.translate("PositionsWindow", u"Number of columns", None))
        self.corners_marking_button.setText(QCoreApplication.translate("PositionsWindow", u"Corners", None))
        self.auto_marking_button.setText(QCoreApplication.translate("PositionsWindow", u"Auto", None))
        self.save_corners_button.setText(QCoreApplication.translate("PositionsWindow", u"Save corners", None))
        self.generate_positions_button.setText(QCoreApplication.translate("PositionsWindow", u"Generate position grid", None))
        self.plot_path_button.setText(QCoreApplication.translate("PositionsWindow", u"Plot", None))
        self.print_corners_button.setText(QCoreApplication.translate("PositionsWindow", u"Print Corners", None))
        self.reload_positions_button.setText(QCoreApplication.translate("PositionsWindow", u"Reload positions", None))
        self.save_positions_button.setText(QCoreApplication.translate("PositionsWindow", u"Save positions ", None))
        self.generate_dummy_button.setText(QCoreApplication.translate("PositionsWindow", u"Gen. dummy positions", None))
        self.save_dummy_button.setText(QCoreApplication.translate("PositionsWindow", u"Save dummy pos", None))
        self.plot_dummy_button.setText(QCoreApplication.translate("PositionsWindow", u"Plot dummy path", None))
        self.rules_group.setTitle(QCoreApplication.translate("PositionsWindow", u"Imaging properties", None))
        self.mm_groups_label.setText(QCoreApplication.translate("PositionsWindow", u"Group", None))
        self.mm_preset_label.setText(QCoreApplication.translate("PositionsWindow", u"Preset", None))
        self.exposure_label.setText(QCoreApplication.translate("PositionsWindow", u"Exposure(ms)", None))
        self.imaging_freq_label.setText(QCoreApplication.translate("PositionsWindow", u"Imaging freq (mins)", None))
        self.add_preset_button.setText(QCoreApplication.translate("PositionsWindow", u"Add", None))
        self.remove_preset_button.setText(QCoreApplication.translate("PositionsWindow", u"Remove", None))
        self.test_acquire_group.setTitle(QCoreApplication.translate("PositionsWindow", u"Test acquire", None))
        self.dont_save_data.setText(QCoreApplication.translate("PositionsWindow", u"Dont save data", None))
        self.simulated_acquisition_check.setText(QCoreApplication.translate("PositionsWindow", u"Put dummy images in queues", None))
        self.save_dir_button.setText(QCoreApplication.translate("PositionsWindow", u"Save dir", None))
        self.mark_positions_group.setTitle(QCoreApplication.translate("PositionsWindow", u"Mark positions", None))
        self.bl_button_1.setText(QCoreApplication.translate("PositionsWindow", u"Bottom Left 1", None))
        self.tl_button_1.setText(QCoreApplication.translate("PositionsWindow", u"Top Left 1", None))
        self.tr_button_1.setText(QCoreApplication.translate("PositionsWindow", u"Top Right 1", None))
        self.br_button_1.setText(QCoreApplication.translate("PositionsWindow", u"Bottom Right 1", None))
        self.tl_button_2.setText(QCoreApplication.translate("PositionsWindow", u"Top Left 2", None))
        self.tr_button_2.setText(QCoreApplication.translate("PositionsWindow", u"Top Right 2", None))
        self.bl_button_2.setText(QCoreApplication.translate("PositionsWindow", u"Bottom Left 2", None))
        self.br_button_2.setText(QCoreApplication.translate("PositionsWindow", u"Bottom Right 2", None))
        self.generate_events_button.setText(QCoreApplication.translate("PositionsWindow", u"Generate Events", None))
        self.preview_events_button.setText(QCoreApplication.translate("PositionsWindow", u"Preview", None))
        self.reset_button.setText(QCoreApplication.translate("PositionsWindow", u"Reset all", None))
        self.close_button.setText(QCoreApplication.translate("PositionsWindow", u"Close", None))
    # retranslateUi

