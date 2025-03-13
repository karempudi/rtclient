# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'run.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_RunWindow(object):
    def setupUi(self, RunWindow):
        if not RunWindow.objectName():
            RunWindow.setObjectName(u"RunWindow")
        RunWindow.resize(303, 338)
        self.centralwidget = QWidget(RunWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 181, 161))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.load_run_button = QPushButton(self.verticalLayoutWidget)
        self.load_run_button.setObjectName(u"load_run_button")

        self.verticalLayout.addWidget(self.load_run_button)

        self.start_run_button = QPushButton(self.verticalLayoutWidget)
        self.start_run_button.setObjectName(u"start_run_button")

        self.verticalLayout.addWidget(self.start_run_button)

        self.stop_run_button = QPushButton(self.verticalLayoutWidget)
        self.stop_run_button.setObjectName(u"stop_run_button")

        self.verticalLayout.addWidget(self.stop_run_button)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 200, 260, 31))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.post_analysis_check = QCheckBox(self.formLayoutWidget)
        self.post_analysis_check.setObjectName(u"post_analysis_check")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.post_analysis_check)

        self.post_save_button = QPushButton(self.formLayoutWidget)
        self.post_save_button.setObjectName(u"post_save_button")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.post_save_button)

        RunWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RunWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 303, 22))
        RunWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RunWindow)
        self.statusbar.setObjectName(u"statusbar")
        RunWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RunWindow)

        QMetaObject.connectSlotsByName(RunWindow)
    # setupUi

    def retranslateUi(self, RunWindow):
        RunWindow.setWindowTitle(QCoreApplication.translate("RunWindow", u"MainWindow", None))
        self.load_run_button.setText(QCoreApplication.translate("RunWindow", u"Load Run parameters", None))
        self.start_run_button.setText(QCoreApplication.translate("RunWindow", u"Start Run", None))
        self.stop_run_button.setText(QCoreApplication.translate("RunWindow", u"Stop Run", None))
        self.post_analysis_check.setText(QCoreApplication.translate("RunWindow", u"Post analysis", None))
        self.post_save_button.setText(QCoreApplication.translate("RunWindow", u"Post Save directory", None))
    # retranslateUi

