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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_TweezerWindow(object):
    def setupUi(self, TweezerWindow):
        if not TweezerWindow.objectName():
            TweezerWindow.setObjectName(u"TweezerWindow")
        TweezerWindow.resize(1487, 845)
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
        self.verticalLayoutWidget_4.setGeometry(QRect(490, 170, 41, 411))
        self.barcode_left_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.barcode_left_layout.setObjectName(u"barcode_left_layout")
        self.barcode_left_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(550, 170, 41, 411))
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
        self.active_traps_list.setGeometry(QRect(680, 490, 241, 281))
        self.active_traps_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tweeze_traps_list = QListWidget(self.centralwidget)
        self.tweeze_traps_list.setObjectName(u"tweeze_traps_list")
        self.tweeze_traps_list.setGeometry(QRect(1050, 490, 241, 281))
        self.tweeze_traps_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.to_tweeze_list_button = QPushButton(self.centralwidget)
        self.to_tweeze_list_button.setObjectName(u"to_tweeze_list_button")
        self.to_tweeze_list_button.setGeometry(QRect(960, 600, 41, 21))
        self.to_active_list_button = QPushButton(self.centralwidget)
        self.to_active_list_button.setObjectName(u"to_active_list_button")
        self.to_active_list_button.setGeometry(QRect(960, 640, 41, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(940, 30, 151, 25))
        self.precompute_forks_button = QPushButton(self.centralwidget)
        self.precompute_forks_button.setObjectName(u"precompute_forks_button")
        self.precompute_forks_button.setGeometry(QRect(1140, 30, 161, 25))
        self.get_traps_button = QPushButton(self.centralwidget)
        self.get_traps_button.setObjectName(u"get_traps_button")
        self.get_traps_button.setGeometry(QRect(940, 530, 89, 25))
        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(940, 560, 89, 25))
        TweezerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TweezerWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1487, 22))
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
        pass
    # retranslateUi

