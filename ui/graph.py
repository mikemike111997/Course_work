# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 951))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 900))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1211, 871))
        self.graphicsView.setSceneRect(QtCore.QRectF(0.0, 0.0, 1200.0, 800.0))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.menuTOPOLOGY = QtWidgets.QMenu(self.menubar)
        self.menuTOPOLOGY.setObjectName("menuTOPOLOGY")
        self.menuSETTING = QtWidgets.QMenu(self.menubar)
        self.menuSETTING.setObjectName("menuSETTING")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiongenerate_random = QtWidgets.QAction(MainWindow)
        self.actiongenerate_random.setObjectName("actiongenerate_random")
        self.actionconfigurations = QtWidgets.QAction(MainWindow)
        self.actionconfigurations.setObjectName("actionconfigurations")
        self.menuTOPOLOGY.addAction(self.actiongenerate_random)
        self.menuSETTING.addAction(self.actionconfigurations)
        self.menubar.addAction(self.menuTOPOLOGY.menuAction())
        self.menubar.addAction(self.menuSETTING.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuTOPOLOGY.setTitle(_translate("MainWindow", "TOPOLOGY"))
        self.menuSETTING.setTitle(_translate("MainWindow", "SETTING"))
        self.actiongenerate_random.setText(_translate("MainWindow", "generate random"))
        self.actionconfigurations.setText(_translate("MainWindow", "configurations"))

