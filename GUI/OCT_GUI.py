# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Temp/OCT_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Get_img as G
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 841, 611))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(871, 10, 231, 611))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

        self.treeView = Mytree(self.splitter)
        self.treeView.setObjectName("treeView")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 1, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_2.addWidget(self.radioButton_6, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout_2.addWidget(self.radioButton_7, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout_2.addWidget(self.radioButton_8, 1, 2, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_2.addWidget(self.radioButton_5, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # ----------------------------------------------------------------------------

        time = QtCore.QDateTime.currentDateTime()
        self.statusbar.showMessage(time)

        self.file_path = None
        self.treeView.doubleClicked.connect(self.show_img)
        self.pushButton.clicked.connect(self.btn_function1)
        self.pushButton.clicked.connect(self.btn_function2)

        self.radioButton.clicked.connect(self.radio_bnt_function1)
        self.radioButton_2.clicked.connect(self.radio_bnt_function2)
        self.radioButton_3.clicked.connect(self.radio_bnt_function3)
        self.radioButton_4.clicked.connect(self.radio_bnt_function4)


        self.model = G.load_model('C:/Users/croma/Desktop/DenseNet121_allfine_5.h5')


        # ----------------------------------------------------------------------------


    def show_img(self, signal):
        self.file_path = self.treeView.model().filePath(signal)
        pixmap = QtGui.QPixmap(self.file_path)
        self.label_5.setPixmap(pixmap)
        self.label.clear()
        self.label_2.clear()
        self.label_3.clear()
        self.label_4.clear()
        self.label_6.clear()

        # self.radioButton_5.setChecked(False)
        # self.radioButton_6.setChecked(False)
        # self.radioButton_7.setChecked(False)
        # self.radioButton_8.setChecked(False)

    def btn_function1(self):
        self.filename = "{}.PNG"
        prediction, y_pred, heatmap = G.Heatmap(self.model, self.file_path)

        self.label.setText("%0.4f" % prediction[0][0])
        self.label_2.setText("%0.4f" % prediction[0][1])
        self.label_3.setText("%0.4f" % prediction[0][2])
        self.label_4.setText("%0.4f" % prediction[0][3])

        if y_pred == 0:
            self.radioButton_5.setChecked(True)
        elif y_pred == 1:
            self.radioButton_6.setChecked(True)
        elif y_pred == 2:
            self.radioButton_7.setChecked(True)
        else:
            self.radioButton_8.setChecked(True)

        G.get_Heatmap(self.file_path, self.filename, heatmap)
        pixmap = QtGui.QPixmap('C:/Users/croma/Desktop/heatmap/' + self.filename)
        self.label_6.setPixmap(pixmap)

    def btn_function2(self):
        pass

    def radio_bnt_function1(self):
        pass

    def radio_bnt_function2(self):
        pass

    def radio_bnt_function3(self):
        pass

    def radio_bnt_function4(self):
        pass


        # ----------------------------------------------------------------------------


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "진단 - 의사"))
        self.radioButton.setText(_translate("MainWindow", "CNV"))
        self.radioButton_2.setText(_translate("MainWindow", "DME"))
        self.radioButton_3.setText(_translate("MainWindow", "DRUSEN"))
        self.radioButton_4.setText(_translate("MainWindow", "NORMAL"))
        self.groupBox_2.setTitle(_translate("MainWindow", "진단 - AI"))
        self.radioButton_6.setText(_translate("MainWindow", "DME :"))
        self.radioButton_7.setText(_translate("MainWindow", "DRUSEN :"))
        self.radioButton_8.setText(_translate("MainWindow", "NORMAL :"))
        self.radioButton_5.setText(_translate("MainWindow", "CNV :"))
        self.pushButton.setText(_translate("MainWindow", "진단"))
        self.pushButton_2.setText(_translate("MainWindow", "결과"))


        # ----------------------------------------------------------------------------


class Mytree(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        super(Mytree, self).__init__(parent)
        tree = QtWidgets.QFileSystemModel()
        tree.setRootPath('C:\\')
        self.setModel(tree)
        self.setRootIndex(tree.index('C:/Users/croma/Desktop/fold'))
        self.setModel(tree)


        # ----------------------------------------------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())