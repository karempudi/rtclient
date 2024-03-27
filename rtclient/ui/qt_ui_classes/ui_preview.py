# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_PreviewWindow(object):
    def setupUi(self, PreviewWindow):
        if not PreviewWindow.objectName():
            PreviewWindow.setObjectName(u"PreviewWindow")
        PreviewWindow.resize(350, 500)
        self.centralwidget = QWidget(PreviewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.preview_list = QListWidget(self.centralwidget)
        self.preview_list.setObjectName(u"preview_list")
        self.preview_list.setGeometry(QRect(10, 10, 311, 391))
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(220, 420, 89, 25))
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(110, 420, 89, 25))
        PreviewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PreviewWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 22))
        PreviewWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PreviewWindow)
        self.statusbar.setObjectName(u"statusbar")
        PreviewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PreviewWindow)

        QMetaObject.connectSlotsByName(PreviewWindow)
    # setupUi

    def retranslateUi(self, PreviewWindow):
        PreviewWindow.setWindowTitle(QCoreApplication.translate("PreviewWindow", u"MainWindow", None))
        self.close_button.setText(QCoreApplication.translate("PreviewWindow", u"Close", None))
        self.save_button.setText(QCoreApplication.translate("PreviewWindow", u"Save", None))
    # retranslateUi

