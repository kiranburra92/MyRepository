from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import SubWin
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.Qt import Qt
import cv2
import SubWinNop
import UIFunctions
import Transformation as filters

# histogram grayscale, log transformation, negative
class Sub_img_nopa(QtWidgets.QMainWindow, SubWinNop.Ui_MainWindow,UIFunctions.SaveFunctions):
    def __init__(self,parent,flag):
        super(Sub_img_nopa, self).__init__(parent)
        self.setupUi(self)
        self.origImage.clicked.connect(self.loadImage)
        self.Run.clicked.connect(self.RunBttn)
        self.destination.clicked.connect(self.getDestButton)
        self.Save.clicked.connect(self.saveButton)
        self.type=flag

    def loadImage(self):
        """
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Select Image for Transformation", "","All Files (*);;Python Files (*.py)",options=options)
        if self.fileName:
            print(self.fileName)
            pixmap = QtGui.QPixmap(self.fileName)
            self.OriginalImage.setScaledContents(True)
            self.OriginalImage.setPixmap(pixmap)
            #self.resize(pixmap.width(),pixmap.height())
            """
        self.fileName=self.DisplayImage(self.OriginalImage)
            

    def RunBttn(self):
        try:
            self.displayProcessedIamge()
        except:
            box=QtWidgets.QMessageBox.about(self,"Select Input Image First","Input image is not selected")
        
    def saveButton(self):
        try:
            saved=self.savetofile(self.savepath,self.img,self.type)
            if saved:
                print('saved')
            else:
                box=QtWidgets.QMessageBox.about(self,"error","Error with save image to disk")
                print('save error')
        except:
            box=QtWidgets.QMessageBox.about(self,"error","please select directory first")
    

    def displayProcessedIamge(self):
        input_image = self.openImage()
        self.img=self.processImage(input_image)

        #pixmap=self.covertnumpyimg(self.img)
        pixmap=self.cvImageToQImage(self.img)
        self.processed.setScaledContents(True)
        self.processed.setPixmap(pixmap)


    def processImage(self,input_image):
        if self.type == 'neg':
            img=filters.Transformation().negative(input_image)
            print("neg")
        elif self.type == 'log':
            img=filters.Transformation().log(input_image)
            print('log')
        elif self.type == 'equal':
            img=filters.Transformation().histogram_equalization(input_image)
            print("equal")
        elif self.type == 'matching':
            img=filters.Transformation().histogram_equalization(input_image)
            print('matching')
        return img

    def openImage(self):
        #input_image = cv2.imread(self.fileName, 1)
        input_image=self.loadImage_color(self.fileName)
        return input_image
    