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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QWidget)

class Ui_TweezerWindow(object):
    def setupUi(self, TweezerWindow):
        if not TweezerWindow.objectName():
            TweezerWindow.setObjectName(u"TweezerWindow")
        TweezerWindow.resize(1039, 677)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TweezerWindow.sizePolicy().hasHeightForWidth())
        TweezerWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(TweezerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.show_button = QPushButton(self.centralwidget)
        self.show_button.setObjectName(u"show_button")
        self.show_button.setGeometry(QRect(650, 80, 181, 25))
        self.image_plot = QGraphicsView(self.centralwidget)
        self.image_plot.setObjectName(u"image_plot")
        self.image_plot.setGeometry(QRect(20, 110, 451, 561))
        self.properties_view = QGraphicsView(self.centralwidget)
        self.properties_view.setObjectName(u"properties_view")
        self.properties_view.setGeometry(QRect(650, 140, 371, 291))
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

        self.radioButton = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton.setObjectName(u"radioButton")

        self.data_to_plot.addWidget(self.radioButton)

        self.cell_tracks_image = QRadioButton(self.horizontalLayoutWidget_2)
        self.cell_tracks_image.setObjectName(u"cell_tracks_image")

        self.data_to_plot.addWidget(self.cell_tracks_image)

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

        self.barcode_plot_1 = QGraphicsView(self.centralwidget)
        self.barcode_plot_1.setObjectName(u"barcode_plot_1")
        self.barcode_plot_1.setGeometry(QRect(490, 150, 51, 471))
        self.barcode_plot_2 = QGraphicsView(self.centralwidget)
        self.barcode_plot_2.setObjectName(u"barcode_plot_2")
        self.barcode_plot_2.setGeometry(QRect(550, 150, 51, 471))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(790, 120, 81, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(520, 120, 67, 17))
        self.show_button_2 = QPushButton(self.centralwidget)
        self.show_button_2.setObjectName(u"show_button_2")
        self.show_button_2.setGeometry(QRect(840, 80, 181, 25))
        TweezerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TweezerWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1039, 22))
        TweezerWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TweezerWindow)
        self.statusbar.setObjectName(u"statusbar")
        TweezerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TweezerWindow)

        QMetaObject.connectSlotsByName(TweezerWindow)
    # setupUi

    def retranslateUi(self, TweezerWindow):
        self.show_button.setText(QCoreApplication.translate("TweezerWindow", u"Plot Current TrapForks", None))
        self.pos_label.setText(QCoreApplication.translate("TweezerWindow", u"Position", None))
        self.ch_no_label.setText(QCoreApplication.translate("TweezerWindow", u"Channel No", None))
        self.fetch_button.setText(QCoreApplication.translate("TweezerWindow", u"Fetch", None))
        self.phase_image.setText(QCoreApplication.translate("TweezerWindow", u"Phase", None))
        self.cell_seg_image.setText(QCoreApplication.translate("TweezerWindow", u"Cell Seg", None))
        self.radioButton.setText(QCoreApplication.translate("TweezerWindow", u"Fluor", None))
        self.cell_tracks_image.setText(QCoreApplication.translate("TweezerWindow", u"Dots", None))
        self.get_last20_radio.setText(QCoreApplication.translate("TweezerWindow", u"Last 20 images", None))
        self.get_all_images_radio.setText(QCoreApplication.translate("TweezerWindow", u"All Images", None))
        self.label.setText(QCoreApplication.translate("TweezerWindow", u"Fork Plots", None))
        self.label_2.setText(QCoreApplication.translate("TweezerWindow", u"Barcodes", None))
        self.show_button_2.setText(QCoreApplication.translate("TweezerWindow", u"All data forks", None))
        pass
    # retranslateUi

