# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubWin_img_equal.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#UI for equalization color
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 613)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.OriginalImage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OriginalImage.sizePolicy().hasHeightForWidth())
        self.OriginalImage.setSizePolicy(sizePolicy)
        self.OriginalImage.setMaximumSize(QtCore.QSize(449, 230))
        self.OriginalImage.setScaledContents(True)
        self.OriginalImage.setObjectName("OriginalImage")
        self.gridLayout.addWidget(self.OriginalImage, 0, 0, 1, 1)
        self.processed = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processed.sizePolicy().hasHeightForWidth())
        self.processed.setSizePolicy(sizePolicy)
        self.processed.setMaximumSize(QtCore.QSize(448, 230))
        self.processed.setObjectName("processed")
        self.gridLayout.addWidget(self.processed, 0, 1, 1, 1)
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setObjectName("Save")
        self.gridLayout.addWidget(self.Save, 3, 1, 1, 1)
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setMinimumSize(QtCore.QSize(0, 32))
        self.Run.setObjectName("Run")
        self.gridLayout.addWidget(self.Run, 2, 1, 1, 1)
        self.origImage = QtWidgets.QPushButton(self.centralwidget)
        self.origImage.setObjectName("origImage")
        self.gridLayout.addWidget(self.origImage, 2, 0, 1, 1)
        self.destination = QtWidgets.QPushButton(self.centralwidget)
        self.destination.setObjectName("destination")
        self.gridLayout.addWidget(self.destination, 3, 0, 1, 1)
        self.hist1 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hist1.sizePolicy().hasHeightForWidth())
        self.hist1.setSizePolicy(sizePolicy)
        self.hist1.setMaximumSize(QtCore.QSize(449, 229))
        self.hist1.setObjectName("hist1")
        self.gridLayout.addWidget(self.hist1, 1, 0, 1, 1)
        self.hist2 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hist2.sizePolicy().hasHeightForWidth())
        self.hist2.setSizePolicy(sizePolicy)
        self.hist2.setMaximumSize(QtCore.QSize(448, 229))
        self.hist2.setObjectName("hist2")
        self.gridLayout.addWidget(self.hist2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 947, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OriginalImage.setText(_translate("MainWindow", "Original Image"))
        self.processed.setText(_translate("MainWindow", "Processed Image"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.origImage.setText(_translate("MainWindow", "Select Image"))
        self.destination.setText(_translate("MainWindow", "Select Directory to Save Transformed Image"))
