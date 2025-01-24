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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

from pyqtgraph import ImageView

class Ui_TweezerWindow(object):
    def setupUi(self, TweezerWindow):
        if not TweezerWindow.objectName():
            TweezerWindow.setObjectName(u"TweezerWindow")
        TweezerWindow.resize(1296, 751)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TweezerWindow.sizePolicy().hasHeightForWidth())
        TweezerWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(TweezerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.current_trap_forks_button = QPushButton(self.centralwidget)
        self.current_trap_forks_button.setObjectName(u"current_trap_forks_button")
        self.current_trap_forks_button.setGeometry(QRect(710, 80, 181, 25))
        self.image_plot = ImageView(self.centralwidget)
        self.image_plot.setObjectName(u"image_plot")
        self.image_plot.setGeometry(QRect(20, 110, 451, 561))
        self.fork_plots_trap = ImageView(self.centralwidget)
        self.fork_plots_trap.setObjectName(u"fork_plots_trap")
        self.fork_plots_trap.setGeometry(QRect(650, 140, 291, 241))
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
        self.phase_image.setChecked(False)

        self.data_to_plot.addWidget(self.phase_image)

        self.cell_seg_image = QRadioButton(self.horizontalLayoutWidget_2)
        self.cell_seg_image.setObjectName(u"cell_seg_image")
        self.cell_seg_image.setChecked(True)

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

        self.barcode_plot_1 = ImageView(self.centralwidget)
        self.barcode_plot_1.setObjectName(u"barcode_plot_1")
        self.barcode_plot_1.setGeometry(QRect(490, 150, 51, 471))
        self.barcode_plot_2 = ImageView(self.centralwidget)
        self.barcode_plot_2.setObjectName(u"barcode_plot_2")
        self.barcode_plot_2.setGeometry(QRect(550, 150, 51, 471))
        self.fork_label = QLabel(self.centralwidget)
        self.fork_label.setObjectName(u"fork_label")
        self.fork_label.setGeometry(QRect(740, 120, 101, 17))
        self.barcodes_label = QLabel(self.centralwidget)
        self.barcodes_label.setObjectName(u"barcodes_label")
        self.barcodes_label.setGeometry(QRect(520, 120, 67, 17))
        self.all_data_forks_button = QPushButton(self.centralwidget)
        self.all_data_forks_button.setObjectName(u"all_data_forks_button")
        self.all_data_forks_button.setGeometry(QRect(1020, 80, 181, 25))
        self.fork_plots_all = ImageView(self.centralwidget)
        self.fork_plots_all.setObjectName(u"fork_plots_all")
        self.fork_plots_all.setGeometry(QRect(960, 140, 281, 241))
        self.fork_label_2 = QLabel(self.centralwidget)
        self.fork_label_2.setObjectName(u"fork_label_2")
        self.fork_label_2.setGeometry(QRect(1050, 120, 121, 17))
        TweezerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TweezerWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1296, 22))
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
        pass
    # retranslateUi

