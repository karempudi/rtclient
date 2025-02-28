# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tweezer.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_TweezerWindow(object):
    def setupUi(self, TweezerWindow):
        if not TweezerWindow.objectName():
            TweezerWindow.setObjectName(u"TweezerWindow")
        TweezerWindow.resize(1803, 895)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TweezerWindow.sizePolicy().hasHeightForWidth())
        TweezerWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(TweezerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.current_trap_forks_button = QPushButton(self.centralwidget)
        self.current_trap_forks_button.setObjectName(u"current_trap_forks_button")
        self.current_trap_forks_button.setGeometry(QRect(740, 80, 181, 25))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 10, 401, 41))
        self.data_to_fetch = QHBoxLayout(self.horizontalLayoutWidget)
        self.data_to_fetch.setObjectName(u"data_to_fetch")
        self.data_to_fetch.setContentsMargins(0, 0, 0, 0)
        self.pos_label = QLabel(self.horizontalLayoutWidget)
        self.pos_label.setObjectName(u"pos_label")

        self.data_to_fetch.addWidget(self.pos_label)

        self.pos_no_edit = QLineEdit(self.horizontalLayoutWidget)
        self.pos_no_edit.setObjectName(u"pos_no_edit")

        self.data_to_fetch.addWidget(self.pos_no_edit)

        self.trap_no_label = QLabel(self.horizontalLayoutWidget)
        self.trap_no_label.setObjectName(u"trap_no_label")

        self.data_to_fetch.addWidget(self.trap_no_label)

        self.trap_no_edit = QLineEdit(self.horizontalLayoutWidget)
        self.trap_no_edit.setObjectName(u"trap_no_edit")

        self.data_to_fetch.addWidget(self.trap_no_edit)

        self.fetch_button = QPushButton(self.horizontalLayoutWidget)
        self.fetch_button.setObjectName(u"fetch_button")

        self.data_to_fetch.addWidget(self.fetch_button)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 60, 491, 41))
        self.data_to_plot = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.data_to_plot.setObjectName(u"data_to_plot")
        self.data_to_plot.setContentsMargins(0, 0, 0, 0)
        self.phase_image = QRadioButton(self.horizontalLayoutWidget_2)
        self.phase_image.setObjectName(u"phase_image")
        self.phase_image.setChecked(True)

        self.data_to_plot.addWidget(self.phase_image)

        self.cell_seg_image = QRadioButton(self.horizontalLayoutWidget_2)
        self.cell_seg_image.setObjectName(u"cell_seg_image")
        self.cell_seg_image.setChecked(False)

        self.data_to_plot.addWidget(self.cell_seg_image)

        self.fluor_image = QRadioButton(self.horizontalLayoutWidget_2)
        self.fluor_image.setObjectName(u"fluor_image")

        self.data_to_plot.addWidget(self.fluor_image)

        self.dots_on_mask_image = QRadioButton(self.horizontalLayoutWidget_2)
        self.dots_on_mask_image.setObjectName(u"dots_on_mask_image")

        self.data_to_plot.addWidget(self.dots_on_mask_image)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(450, 10, 230, 41))
        self.image_show_layout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.image_show_layout.setObjectName(u"image_show_layout")
        self.image_show_layout.setContentsMargins(0, 0, 0, 0)
        self.get_last20_radio = QRadioButton(self.horizontalLayoutWidget_4)
        self.get_last20_radio.setObjectName(u"get_last20_radio")
        self.get_last20_radio.setChecked(True)

        self.image_show_layout.addWidget(self.get_last20_radio)

        self.get_all_images_radio = QRadioButton(self.horizontalLayoutWidget_4)
        self.get_all_images_radio.setObjectName(u"get_all_images_radio")

        self.image_show_layout.addWidget(self.get_all_images_radio)

        self.fork_label = QLabel(self.centralwidget)
        self.fork_label.setObjectName(u"fork_label")
        self.fork_label.setGeometry(QRect(780, 130, 101, 17))
        self.barcodes_label = QLabel(self.centralwidget)
        self.barcodes_label.setObjectName(u"barcodes_label")
        self.barcodes_label.setGeometry(QRect(510, 110, 67, 17))
        self.all_data_forks_button = QPushButton(self.centralwidget)
        self.all_data_forks_button.setObjectName(u"all_data_forks_button")
        self.all_data_forks_button.setGeometry(QRect(1120, 80, 181, 25))
        self.fork_label_2 = QLabel(self.centralwidget)
        self.fork_label_2.setObjectName(u"fork_label_2")
        self.fork_label_2.setGeometry(QRect(1160, 130, 121, 17))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(640, 160, 371, 321))
        self.single_trap_fork_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.single_trap_fork_layout.setObjectName(u"single_trap_fork_layout")
        self.single_trap_fork_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1030, 160, 361, 321))
        self.all_data_fork_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.all_data_fork_layout.setObjectName(u"all_data_fork_layout")
        self.all_data_fork_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(30, 130, 421, 541))
        self.image_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.image_layout.setObjectName(u"image_layout")
        self.image_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(490, 170, 41, 321))
        self.barcode_left_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.barcode_left_layout.setObjectName(u"barcode_left_layout")
        self.barcode_left_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(550, 170, 41, 321))
        self.barcode_right_layout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.barcode_right_layout.setObjectName(u"barcode_right_layout")
        self.barcode_right_layout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(500, 140, 31, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(550, 140, 41, 17))
        self.active_traps_list = QListWidget(self.centralwidget)
        self.active_traps_list.setObjectName(u"active_traps_list")
        self.active_traps_list.setGeometry(QRect(660, 510, 241, 281))
        self.active_traps_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tweeze_traps_list = QListWidget(self.centralwidget)
        self.tweeze_traps_list.setObjectName(u"tweeze_traps_list")
        self.tweeze_traps_list.setGeometry(QRect(1020, 510, 241, 281))
        self.tweeze_traps_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.to_tweeze_list_button = QPushButton(self.centralwidget)
        self.to_tweeze_list_button.setObjectName(u"to_tweeze_list_button")
        self.to_tweeze_list_button.setGeometry(QRect(940, 600, 41, 21))
        self.to_active_list_button = QPushButton(self.centralwidget)
        self.to_active_list_button.setObjectName(u"to_active_list_button")
        self.to_active_list_button.setGeometry(QRect(940, 640, 41, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(940, 30, 151, 25))
        self.precompute_forks_button = QPushButton(self.centralwidget)
        self.precompute_forks_button.setObjectName(u"precompute_forks_button")
        self.precompute_forks_button.setGeometry(QRect(1140, 30, 161, 25))
        self.get_traps_button = QPushButton(self.centralwidget)
        self.get_traps_button.setObjectName(u"get_traps_button")
        self.get_traps_button.setGeometry(QRect(920, 530, 89, 25))
        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(920, 560, 89, 25))
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(470, 520, 181, 205))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.metrics_label = QLabel(self.formLayoutWidget)
        self.metrics_label.setObjectName(u"metrics_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.metrics_label)

        self.ssim_edit = QLineEdit(self.formLayoutWidget)
        self.ssim_edit.setObjectName(u"ssim_edit")
        self.ssim_edit.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ssim_edit)

        self.moran_label = QLabel(self.formLayoutWidget)
        self.moran_label.setObjectName(u"moran_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.moran_label)

        self.moran_edit = QLineEdit(self.formLayoutWidget)
        self.moran_edit.setObjectName(u"moran_edit")
        self.moran_edit.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.moran_edit)

        self.sobolev_label = QLabel(self.formLayoutWidget)
        self.sobolev_label.setObjectName(u"sobolev_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.sobolev_label)

        self.sobolev_edit = QLineEdit(self.formLayoutWidget)
        self.sobolev_edit.setObjectName(u"sobolev_edit")
        self.sobolev_edit.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.sobolev_edit)

        self.energy_label = QLabel(self.formLayoutWidget)
        self.energy_label.setObjectName(u"energy_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.energy_label)

        self.energy_edit = QLineEdit(self.formLayoutWidget)
        self.energy_edit.setObjectName(u"energy_edit")
        self.energy_edit.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.energy_edit)

        self.corrleation_label = QLabel(self.formLayoutWidget)
        self.corrleation_label.setObjectName(u"corrleation_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.corrleation_label)

        self.correlation_edit = QLineEdit(self.formLayoutWidget)
        self.correlation_edit.setObjectName(u"correlation_edit")
        self.correlation_edit.setReadOnly(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.correlation_edit)

        self.ks_edit = QLineEdit(self.formLayoutWidget)
        self.ks_edit.setObjectName(u"ks_edit")
        self.ks_edit.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ks_edit)

        self.ks_label = QLabel(self.formLayoutWidget)
        self.ks_label.setObjectName(u"ks_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.ks_label)

        self.ssim_label = QLabel(self.formLayoutWidget)
        self.ssim_label.setObjectName(u"ssim_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.ssim_label)

        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(1320, 490, 371, 341))
        self.score_plot_layout = QVBoxLayout(self.verticalLayoutWidget_6)
        self.score_plot_layout.setObjectName(u"score_plot_layout")
        self.score_plot_layout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(740, 490, 91, 17))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1090, 490, 111, 17))
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(1420, 160, 351, 300))
        self.threshold_layout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.threshold_layout.setObjectName(u"threshold_layout")
        self.threshold_layout.setContentsMargins(0, 0, 0, 0)
        self.threshold_radios_layout = QVBoxLayout()
        self.threshold_radios_layout.setObjectName(u"threshold_radios_layout")
        self.correlation_radio = QRadioButton(self.horizontalLayoutWidget_3)
        self.correlation_radio.setObjectName(u"correlation_radio")
        self.correlation_radio.setEnabled(True)
        self.correlation_radio.setChecked(True)

        self.threshold_radios_layout.addWidget(self.correlation_radio)

        self.moran_radio = QRadioButton(self.horizontalLayoutWidget_3)
        self.moran_radio.setObjectName(u"moran_radio")
        self.moran_radio.setChecked(False)

        self.threshold_radios_layout.addWidget(self.moran_radio)

        self.sobolev_radio = QRadioButton(self.horizontalLayoutWidget_3)
        self.sobolev_radio.setObjectName(u"sobolev_radio")

        self.threshold_radios_layout.addWidget(self.sobolev_radio)

        self.ssim_radio = QRadioButton(self.horizontalLayoutWidget_3)
        self.ssim_radio.setObjectName(u"ssim_radio")

        self.threshold_radios_layout.addWidget(self.ssim_radio)

        self.kolmogorov_radio = QRadioButton(self.horizontalLayoutWidget_3)
        self.kolmogorov_radio.setObjectName(u"kolmogorov_radio")

        self.threshold_radios_layout.addWidget(self.kolmogorov_radio)

        self.energy_radio = QRadioButton(self.horizontalLayoutWidget_3)
        self.energy_radio.setObjectName(u"energy_radio")

        self.threshold_radios_layout.addWidget(self.energy_radio)


        self.threshold_layout.addLayout(self.threshold_radios_layout)

        self.threshold_sliders_layout = QVBoxLayout()
        self.threshold_sliders_layout.setObjectName(u"threshold_sliders_layout")

        self.threshold_layout.addLayout(self.threshold_sliders_layout)

        self.threshold_values_layout = QVBoxLayout()
        self.threshold_values_layout.setObjectName(u"threshold_values_layout")
        self.correlation_value_label = QLabel(self.horizontalLayoutWidget_3)
        self.correlation_value_label.setObjectName(u"correlation_value_label")

        self.threshold_values_layout.addWidget(self.correlation_value_label)

        self.moran_value_label = QLabel(self.horizontalLayoutWidget_3)
        self.moran_value_label.setObjectName(u"moran_value_label")

        self.threshold_values_layout.addWidget(self.moran_value_label)

        self.sobolev_value_label = QLabel(self.horizontalLayoutWidget_3)
        self.sobolev_value_label.setObjectName(u"sobolev_value_label")

        self.threshold_values_layout.addWidget(self.sobolev_value_label)

        self.ssim_value_label = QLabel(self.horizontalLayoutWidget_3)
        self.ssim_value_label.setObjectName(u"ssim_value_label")

        self.threshold_values_layout.addWidget(self.ssim_value_label)

        self.kolmogorov_value_label = QLabel(self.horizontalLayoutWidget_3)
        self.kolmogorov_value_label.setObjectName(u"kolmogorov_value_label")

        self.threshold_values_layout.addWidget(self.kolmogorov_value_label)

        self.energy_value_label = QLabel(self.horizontalLayoutWidget_3)
        self.energy_value_label.setObjectName(u"energy_value_label")

        self.threshold_values_layout.addWidget(self.energy_value_label)


        self.threshold_layout.addLayout(self.threshold_values_layout)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(910, 690, 101, 25))
        self.apply_filters_check = QCheckBox(self.centralwidget)
        self.apply_filters_check.setObjectName(u"apply_filters_check")
        self.apply_filters_check.setGeometry(QRect(1510, 110, 111, 23))
        self.active_traps_counter = QLineEdit(self.centralwidget)
        self.active_traps_counter.setObjectName(u"active_traps_counter")
        self.active_traps_counter.setGeometry(QRect(760, 800, 113, 25))
        self.active_traps_counter.setReadOnly(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(680, 800, 67, 17))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1030, 800, 67, 17))
        self.tweeze_traps_counter = QLineEdit(self.centralwidget)
        self.tweeze_traps_counter.setObjectName(u"tweeze_traps_counter")
        self.tweeze_traps_counter.setGeometry(QRect(1100, 800, 113, 25))
        self.tweeze_traps_counter.setReadOnly(True)
        TweezerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TweezerWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1803, 22))
        TweezerWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TweezerWindow)
        self.statusbar.setObjectName(u"statusbar")
        TweezerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TweezerWindow)

        QMetaObject.connectSlotsByName(TweezerWindow)
    # setupUi

    def retranslateUi(self, TweezerWindow):
        self.current_trap_forks_button.setText(QCoreApplication.translate("TweezerWindow", u"Plot Current TrapForks", None))
        self.pos_label.setText(QCoreApplication.translate("TweezerWindow", u"Position", None))
        self.trap_no_label.setText(QCoreApplication.translate("TweezerWindow", u"Trap No", None))
        self.fetch_button.setText(QCoreApplication.translate("TweezerWindow", u"Fetch", None))
        self.phase_image.setText(QCoreApplication.translate("TweezerWindow", u"Phase", None))
        self.cell_seg_image.setText(QCoreApplication.translate("TweezerWindow", u"Cell Seg", None))
        self.fluor_image.setText(QCoreApplication.translate("TweezerWindow", u"Fluor", None))
        self.dots_on_mask_image.setText(QCoreApplication.translate("TweezerWindow", u"Dots on mask", None))
        self.get_last20_radio.setText(QCoreApplication.translate("TweezerWindow", u"Last 20 images", None))
        self.get_all_images_radio.setText(QCoreApplication.translate("TweezerWindow", u"All Images", None))
        self.fork_label.setText(QCoreApplication.translate("TweezerWindow", u"Trap fork plot", None))
        self.barcodes_label.setText(QCoreApplication.translate("TweezerWindow", u"Barcodes", None))
        self.all_data_forks_button.setText(QCoreApplication.translate("TweezerWindow", u"All data forks", None))
        self.fork_label_2.setText(QCoreApplication.translate("TweezerWindow", u"All data fork plot", None))
        self.label.setText(QCoreApplication.translate("TweezerWindow", u"Left", None))
        self.label_2.setText(QCoreApplication.translate("TweezerWindow", u"Right", None))
        self.to_tweeze_list_button.setText(QCoreApplication.translate("TweezerWindow", u">>", None))
        self.to_active_list_button.setText(QCoreApplication.translate("TweezerWindow", u"<<", None))
        self.pushButton.setText(QCoreApplication.translate("TweezerWindow", u"Convert to Polars", None))
        self.precompute_forks_button.setText(QCoreApplication.translate("TweezerWindow", u"Pre-compute forks", None))
        self.get_traps_button.setText(QCoreApplication.translate("TweezerWindow", u"Get all traps", None))
        self.reset_button.setText(QCoreApplication.translate("TweezerWindow", u"Reset", None))
        self.metrics_label.setText(QCoreApplication.translate("TweezerWindow", u"Metrics", None))
        self.moran_label.setText(QCoreApplication.translate("TweezerWindow", u"Moran", None))
        self.sobolev_label.setText(QCoreApplication.translate("TweezerWindow", u"Sobolev", None))
        self.energy_label.setText(QCoreApplication.translate("TweezerWindow", u"Energy", None))
        self.corrleation_label.setText(QCoreApplication.translate("TweezerWindow", u"Correlation", None))
        self.ks_label.setText(QCoreApplication.translate("TweezerWindow", u"Kolmogorov", None))
        self.ssim_label.setText(QCoreApplication.translate("TweezerWindow", u"SSIM", None))
        self.label_3.setText(QCoreApplication.translate("TweezerWindow", u"All traps list", None))
        self.label_4.setText(QCoreApplication.translate("TweezerWindow", u"Selectetd traps", None))
        self.correlation_radio.setText(QCoreApplication.translate("TweezerWindow", u"Correlation", None))
        self.moran_radio.setText(QCoreApplication.translate("TweezerWindow", u"Moran", None))
        self.sobolev_radio.setText(QCoreApplication.translate("TweezerWindow", u"Sobolev", None))
        self.ssim_radio.setText(QCoreApplication.translate("TweezerWindow", u"SSIM", None))
        self.kolmogorov_radio.setText(QCoreApplication.translate("TweezerWindow", u"Kolmogorov", None))
        self.energy_radio.setText(QCoreApplication.translate("TweezerWindow", u"Energy", None))
        self.correlation_value_label.setText(QCoreApplication.translate("TweezerWindow", u"Value:", None))
        self.moran_value_label.setText(QCoreApplication.translate("TweezerWindow", u"Value:", None))
        self.sobolev_value_label.setText(QCoreApplication.translate("TweezerWindow", u"Value:", None))
        self.ssim_value_label.setText(QCoreApplication.translate("TweezerWindow", u"Value:", None))
        self.kolmogorov_value_label.setText(QCoreApplication.translate("TweezerWindow", u"Value:", None))
        self.energy_value_label.setText(QCoreApplication.translate("TweezerWindow", u"Value:", None))
        self.pushButton_2.setText(QCoreApplication.translate("TweezerWindow", u"Save selection", None))
        self.apply_filters_check.setText(QCoreApplication.translate("TweezerWindow", u"Apply Filters", None))
        self.label_5.setText(QCoreApplication.translate("TweezerWindow", u"Count:", None))
        self.label_6.setText(QCoreApplication.translate("TweezerWindow", u"Count:", None))
        pass
    # retranslateUi

