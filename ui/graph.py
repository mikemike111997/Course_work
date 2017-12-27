# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
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
        self.graphicsView.setGeometry(QtCore.QRect(0, 190, 1211, 681))
        self.graphicsView.setSceneRect(QtCore.QRectF(0.0, 0.0, 1200.0, 800.0))
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 751, 173))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dst_sb = QtWidgets.QSpinBox(self.layoutWidget)
        self.dst_sb.setObjectName("dst_sb")
        self.horizontalLayout.addWidget(self.dst_sb)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.src_sb = QtWidgets.QSpinBox(self.layoutWidget)
        self.src_sb.setObjectName("src_sb")
        self.horizontalLayout_2.addWidget(self.src_sb)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.send_msg_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.send_msg_btn.setObjectName("send_msg_btn")
        self.gridLayout_2.addWidget(self.send_msg_btn, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.result_textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.result_textBrowser.setObjectName("result_textBrowser")
        self.verticalLayout_3.addWidget(self.result_textBrowser)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 3, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.package_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.package_spinBox.setMaximum(1024)
        self.package_spinBox.setProperty("value", 64)
        self.package_spinBox.setObjectName("package_spinBox")
        self.verticalLayout_5.addWidget(self.package_spinBox)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.service_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.service_spinBox.setMaximum(1024)
        self.service_spinBox.setProperty("value", 4)
        self.service_spinBox.setObjectName("service_spinBox")
        self.verticalLayout_4.addWidget(self.service_spinBox)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.layoutWidget.raise_()
        self.graphicsView.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.package_spinBox.raise_()
        self.service_spinBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
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
        self.label.setText(_translate("MainWindow", "Send msg"))
        self.label_4.setText(_translate("MainWindow", "msg:"))
        self.label_3.setText(_translate("MainWindow", "dst:"))
        self.label_2.setText(_translate("MainWindow", "src:"))
        self.label_5.setText(_translate("MainWindow", "Режим:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Віртуальний режим"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Дейтаграмний режим"))
        self.send_msg_btn.setText(_translate("MainWindow", "Send!"))
        self.label_6.setText(_translate("MainWindow", "Результат:"))
        self.label_7.setText(_translate("MainWindow", "Package size(bytes):"))
        self.label_8.setText(_translate("MainWindow", "service data size(bytes):"))
        self.menuTOPOLOGY.setTitle(_translate("MainWindow", "TOPOLOGY"))
        self.menuSETTING.setTitle(_translate("MainWindow", "SETTING"))
        self.actiongenerate_random.setText(_translate("MainWindow", "generate random"))
        self.actionconfigurations.setText(_translate("MainWindow", "configurations"))

