from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import SubWin
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.Qt import Qt
import cv2
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import SubWin_equal_UI
import UIFunctions
import Transformation as filters


# equalization color
class Sub_equal_color(QtWidgets.QMainWindow, SubWin_equal_UI.Ui_MainWindow,UIFunctions.SaveFunctions):
    def __init__(self,parent,flag):
        super(Sub_equal_color, self).__init__(parent)
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
            self.displayHisto_normalize_before()
            self.displayHisto_normalize_after()

        except:
            box=QtWidgets.QMessageBox.about(self,"Select Input Image First","Input image is not selected")
    


    def saveButton(self):

        try:
            saved=self.savetofile(self.savepath,self.img,self.type)
            self.savehistofile_color(self.savepath,self.hists_before,'Original Image')
            self.savehistofile_color(self.savepath,self.hists_after,'Processed Image')
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

        pixmap=self.cvImageToQImage(self.img)
        self.processed.setScaledContents(True)
        self.processed.setPixmap(pixmap)


    def displayHisto_normalize_before(self):
        input_image = self.openImage()
        self.hists_before=filters.Transformation().compute_histogram_color(input_image)
        self.hist_norm_R=filters.Transformation().histogram_equalization_normalize_color(self.hists_before[0],input_image)
        self.hist_norm_G=filters.Transformation().histogram_equalization_normalize_color(self.hists_before[1],input_image)
        self.hist_norm_B=filters.Transformation().histogram_equalization_normalize_color(self.hists_before[2],input_image)
        scene = QtWidgets.QGraphicsScene(self)
        figure = Figure()
        axes = figure.gca()
        axes.set_color_cycle(['red', 'green', 'blue'])
        axes.set_title("Histogram of Original Image")
        axes.plot(self.hist_norm_R)
        axes.plot(self.hist_norm_G)
        axes.plot(self.hist_norm_B)
        #axes.legend(['Red Color', 'Green Color', 'Blue Color'], loc='upper left')
        canvas = FigureCanvas(figure)
        canvas.setGeometry(0, 0, 430, 220)
        scene.addWidget(canvas)
        self.hist1.setScene(scene)

    def displayHisto_normalize_after(self):
        self.hists_after=filters.Transformation().compute_histogram_color(self.img)
        self.hist_norm_R=filters.Transformation().histogram_equalization_normalize_color(self.hists_after[0],self.img)
        self.hist_norm_G=filters.Transformation().histogram_equalization_normalize_color(self.hists_after[1],self.img)
        self.hist_norm_B=filters.Transformation().histogram_equalization_normalize_color(self.hists_after[2],self.img)
        scene = QtWidgets.QGraphicsScene(self)
        figure = Figure()
        axes = figure.gca()
        axes.set_color_cycle(['red', 'green', 'blue'])
        axes.set_title("Normalized Histogram of Processed Image")
        axes.plot(self.hist_norm_R)
        axes.plot(self.hist_norm_G)
        axes.plot(self.hist_norm_B)
        #axes.legend(['Red Color', 'Green Color', 'Blue Color'], loc='upper left')
        canvas = FigureCanvas(figure)
        canvas.setGeometry(0, 0, 430, 220)
        scene.addWidget(canvas)
        self.hist2.setScene(scene)

    def displayHisto_cumulative(self):
        input_image = self.openImage()
        self.hist_cum=filters.Transformation().histogram_equalization_cumulative(input_image)
        scene = QtWidgets.QGraphicsScene(self)
        #self.scene = scene
        figure = Figure()
        axes = figure.gca()
        axes.set_title("Normalized Histogram")
        axes.plot(self.hist_cum)
        canvas = FigureCanvas(figure)
        canvas.setGeometry(0, 0, 430, 220)
        scene.addWidget(canvas)
        self.hist2.setScene(scene)


    def processImage(self,input_image):
        self.img=filters.Transformation().histogram_equalization_color(input_image)
        print("equal")
        return self.img

    def openImage(self):
        #input_image = cv2.imread(self.fileName)
        input_image=self.loadImage_color(self.fileName)
        print(input_image.dtype)
        return input_image

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Sub_equal_color(None,'equal')
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()