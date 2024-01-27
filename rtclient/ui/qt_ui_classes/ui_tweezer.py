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
    QGraphicsView, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QStatusBar, QVBoxLayout, QWidget)

class Ui_TweezerWindow(object):
    def setupUi(self, TweezerWindow):
        if not TweezerWindow.objectName():
            TweezerWindow.setObjectName(u"TweezerWindow")
        TweezerWindow.resize(1551, 709)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TweezerWindow.sizePolicy().hasHeightForWidth())
        TweezerWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(TweezerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.remove_button = QPushButton(self.centralwidget)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setGeometry(QRect(1090, 450, 89, 25))
        self.show_button = QPushButton(self.centralwidget)
        self.show_button.setObjectName(u"show_button")
        self.show_button.setGeometry(QRect(990, 450, 89, 25))
        self.undo_button = QPushButton(self.centralwidget)
        self.undo_button.setObjectName(u"undo_button")
        self.undo_button.setGeometry(QRect(990, 490, 89, 25))
        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(1090, 490, 89, 25))
        self.image_plot = QGraphicsView(self.centralwidget)
        self.image_plot.setObjectName(u"image_plot")
        self.image_plot.setGeometry(QRect(20, 110, 451, 561))
        self.filter_params_box = QGroupBox(self.centralwidget)
        self.filter_params_box.setObjectName(u"filter_params_box")
        self.filter_params_box.setGeometry(QRect(660, 80, 291, 251))
        self.formLayoutWidget = QWidget(self.filter_params_box)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 30, 261, 201))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_label = QLabel(self.formLayoutWidget)
        self.frame_label.setObjectName(u"frame_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame_label)

        self.area_label = QLabel(self.formLayoutWidget)
        self.area_label.setObjectName(u"area_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.area_label)

        self.fraction_label = QLabel(self.formLayoutWidget)
        self.fraction_label.setObjectName(u"fraction_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.fraction_label)

        self.area_slider = QSlider(self.formLayoutWidget)
        self.area_slider.setObjectName(u"area_slider")
        self.area_slider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.area_slider)

        self.fraction_slider = QSlider(self.formLayoutWidget)
        self.fraction_slider.setObjectName(u"fraction_slider")
        self.fraction_slider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.fraction_slider)

        self.cell_obj_label = QLabel(self.formLayoutWidget)
        self.cell_obj_label.setObjectName(u"cell_obj_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.cell_obj_label)

        self.cell_obj_slider = QSlider(self.formLayoutWidget)
        self.cell_obj_slider.setObjectName(u"cell_obj_slider")
        self.cell_obj_slider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cell_obj_slider)

        self.frame_slider = QSlider(self.formLayoutWidget)
        self.frame_slider.setObjectName(u"frame_slider")
        self.frame_slider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame_slider)

        self.next_auto_button = QPushButton(self.centralwidget)
        self.next_auto_button.setObjectName(u"next_auto_button")
        self.next_auto_button.setGeometry(QRect(1090, 530, 89, 25))
        self.send_tweeze_pos_button = QPushButton(self.centralwidget)
        self.send_tweeze_pos_button.setObjectName(u"send_tweeze_pos_button")
        self.send_tweeze_pos_button.setGeometry(QRect(980, 630, 191, 25))
        self.properties_view = QGraphicsView(self.centralwidget)
        self.properties_view.setObjectName(u"properties_view")
        self.properties_view.setGeometry(QRect(650, 440, 321, 211))
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

        self.ch_no_label = QLabel(self.horizontalLayoutWidget)
        self.ch_no_label.setObjectName(u"ch_no_label")

        self.data_to_fetch.addWidget(self.ch_no_label)

        self.ch_no_edit = QLineEdit(self.horizontalLayoutWidget)
        self.ch_no_edit.setObjectName(u"ch_no_edit")

        self.data_to_fetch.addWidget(self.ch_no_edit)

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
        self.phase_image.setChecked(False)

        self.data_to_plot.addWidget(self.phase_image)

        self.cell_seg_image = QRadioButton(self.horizontalLayoutWidget_2)
        self.cell_seg_image.setObjectName(u"cell_seg_image")
        self.cell_seg_image.setChecked(True)

        self.data_to_plot.addWidget(self.cell_seg_image)

        self.cell_tracks_image = QRadioButton(self.horizontalLayoutWidget_2)
        self.cell_tracks_image.setObjectName(u"cell_tracks_image")

        self.data_to_plot.addWidget(self.cell_tracks_image)

        self.expt_running_check = QCheckBox(self.centralwidget)
        self.expt_running_check.setObjectName(u"expt_running_check")
        self.expt_running_check.setGeometry(QRect(460, 20, 131, 23))
        self.active_pos_list = QListWidget(self.centralwidget)
        self.active_pos_list.setObjectName(u"active_pos_list")
        self.active_pos_list.setGeometry(QRect(970, 10, 256, 421))
        self.active_pos_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tweeze_pos_list = QListWidget(self.centralwidget)
        self.tweeze_pos_list.setObjectName(u"tweeze_pos_list")
        self.tweeze_pos_list.setGeometry(QRect(1280, 10, 256, 421))
        self.tweeze_pos_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.toTweezeListButton = QPushButton(self.centralwidget)
        self.toTweezeListButton.setObjectName(u"toTweezeListButton")
        self.toTweezeListButton.setGeometry(QRect(1230, 210, 41, 21))
        self.to_active_list_button = QPushButton(self.centralwidget)
        self.to_active_list_button.setObjectName(u"to_active_list_button")
        self.to_active_list_button.setGeometry(QRect(1230, 270, 41, 21))
        self.view_active_list_check = QCheckBox(self.centralwidget)
        self.view_active_list_check.setObjectName(u"view_active_list_check")
        self.view_active_list_check.setGeometry(QRect(1000, 580, 92, 23))
        self.view_active_list_check.setChecked(True)
        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(620, 10, 230, 41))
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

        self.plot_properties_check = QCheckBox(self.centralwidget)
        self.plot_properties_check.setObjectName(u"plot_properties_check")
        self.plot_properties_check.setGeometry(QRect(1090, 580, 121, 23))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(670, 350, 281, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.find_tweezable_pos_button = QPushButton(self.verticalLayoutWidget)
        self.find_tweezable_pos_button.setObjectName(u"find_tweezable_pos_button")

        self.verticalLayout.addWidget(self.find_tweezable_pos_button)

        self.update_filters_button = QPushButton(self.verticalLayoutWidget)
        self.update_filters_button.setObjectName(u"update_filters_button")

        self.verticalLayout.addWidget(self.update_filters_button)

        self.barcode_plot_1 = QGraphicsView(self.centralwidget)
        self.barcode_plot_1.setObjectName(u"barcode_plot_1")
        self.barcode_plot_1.setGeometry(QRect(490, 150, 51, 471))
        self.barcode_plot_2 = QGraphicsView(self.centralwidget)
        self.barcode_plot_2.setObjectName(u"barcode_plot_2")
        self.barcode_plot_2.setGeometry(QRect(550, 150, 51, 471))
        TweezerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TweezerWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1551, 22))
        TweezerWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TweezerWindow)
        self.statusbar.setObjectName(u"statusbar")
        TweezerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TweezerWindow)

        QMetaObject.connectSlotsByName(TweezerWindow)
    # setupUi

    def retranslateUi(self, TweezerWindow):
        self.remove_button.setText(QCoreApplication.translate("TweezerWindow", u"Remove", None))
        self.show_button.setText(QCoreApplication.translate("TweezerWindow", u"Show", None))
        self.undo_button.setText(QCoreApplication.translate("TweezerWindow", u"Undo", None))
        self.reset_button.setText(QCoreApplication.translate("TweezerWindow", u"Reset", None))
        self.filter_params_box.setTitle(QCoreApplication.translate("TweezerWindow", u"Filter Parameters", None))
        self.frame_label.setText(QCoreApplication.translate("TweezerWindow", u"Starting Frame No", None))
        self.area_label.setText(QCoreApplication.translate("TweezerWindow", u"Area Threshold", None))
        self.fraction_label.setText(QCoreApplication.translate("TweezerWindow", u"Fraction", None))
        self.cell_obj_label.setText(QCoreApplication.translate("TweezerWindow", u"No of Cell like objects", None))
        self.next_auto_button.setText(QCoreApplication.translate("TweezerWindow", u"Next Auto", None))
        self.send_tweeze_pos_button.setText(QCoreApplication.translate("TweezerWindow", u"Send Tweeze Positions", None))
        self.pos_label.setText(QCoreApplication.translate("TweezerWindow", u"Position", None))
        self.ch_no_label.setText(QCoreApplication.translate("TweezerWindow", u"Channel No", None))
        self.fetch_button.setText(QCoreApplication.translate("TweezerWindow", u"Fetch", None))
        self.phase_image.setText(QCoreApplication.translate("TweezerWindow", u"Phase", None))
        self.cell_seg_image.setText(QCoreApplication.translate("TweezerWindow", u"Cell Seg", None))
        self.cell_tracks_image.setText(QCoreApplication.translate("TweezerWindow", u"Tracking", None))
        self.expt_running_check.setText(QCoreApplication.translate("TweezerWindow", u"Is Expt running?", None))
        self.toTweezeListButton.setText(QCoreApplication.translate("TweezerWindow", u">>", None))
        self.to_active_list_button.setText(QCoreApplication.translate("TweezerWindow", u"<<", None))
        self.view_active_list_check.setText(QCoreApplication.translate("TweezerWindow", u"Active? ", None))
        self.get_last20_radio.setText(QCoreApplication.translate("TweezerWindow", u"Last 20 images", None))
        self.get_all_images_radio.setText(QCoreApplication.translate("TweezerWindow", u"All Images", None))
        self.plot_properties_check.setText(QCoreApplication.translate("TweezerWindow", u"Plot Properties", None))
        self.find_tweezable_pos_button.setText(QCoreApplication.translate("TweezerWindow", u"Find All Tweezable Channels", None))
        self.update_filters_button.setText(QCoreApplication.translate("TweezerWindow", u"Update Filter Parameters", None))
        pass
    # retranslateUi

