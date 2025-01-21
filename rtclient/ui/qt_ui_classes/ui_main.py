# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(546, 313)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(390, 10, 121, 141))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 30, 91, 101))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.live_button = QPushButton(self.verticalLayoutWidget_2)
        self.live_button.setObjectName(u"live_button")

        self.verticalLayout_2.addWidget(self.live_button)

        self.tweezer_button = QPushButton(self.verticalLayoutWidget_2)
        self.tweezer_button.setObjectName(u"tweezer_button")

        self.verticalLayout_2.addWidget(self.tweezer_button)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(180, 10, 20, 171))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(370, 10, 20, 171))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(520, 10, 20, 171))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 10, 171, 171))
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 30, 154, 131))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.positions_button = QPushButton(self.verticalLayoutWidget_3)
        self.positions_button.setObjectName(u"positions_button")

        self.verticalLayout_3.addWidget(self.positions_button)

        self.rules_button = QPushButton(self.verticalLayoutWidget_3)
        self.rules_button.setObjectName(u"rules_button")

        self.verticalLayout_3.addWidget(self.rules_button)

        self.preview_button = QPushButton(self.verticalLayoutWidget_3)
        self.preview_button.setObjectName(u"preview_button")

        self.verticalLayout_3.addWidget(self.preview_button)

        self.parameters_button = QPushButton(self.verticalLayoutWidget_3)
        self.parameters_button.setObjectName(u"parameters_button")

        self.verticalLayout_3.addWidget(self.parameters_button)

        self.quit_button = QPushButton(self.centralwidget)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setGeometry(QRect(140, 230, 89, 25))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(200, 30, 161, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.write_run_params_button = QPushButton(self.verticalLayoutWidget)
        self.write_run_params_button.setObjectName(u"write_run_params_button")

        self.verticalLayout.addWidget(self.write_run_params_button)

        self.load_run_params_button = QPushButton(self.verticalLayoutWidget)
        self.load_run_params_button.setObjectName(u"load_run_params_button")

        self.verticalLayout.addWidget(self.load_run_params_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 546, 22))
        self.menubar.setNativeMenuBar(True)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
        self.live_button.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.tweezer_button.setText(QCoreApplication.translate("MainWindow", u"Tweeze", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.positions_button.setText(QCoreApplication.translate("MainWindow", u"Positions", None))
        self.rules_button.setText(QCoreApplication.translate("MainWindow", u"Rules", None))
        self.preview_button.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.parameters_button.setText(QCoreApplication.translate("MainWindow", u"Analysis(parameters)", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.write_run_params_button.setText(QCoreApplication.translate("MainWindow", u"Write Run parameters", None))
        self.load_run_params_button.setText(QCoreApplication.translate("MainWindow", u"Load Run parameters", None))
    # retranslateUi

