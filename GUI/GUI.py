# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Temp\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import SAINT_RESULT_CODE as S
import keras


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = Mytree(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(586, 10, 235, 521))
        self.treeView.setObjectName("treeView")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 571, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menufile.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton = Mybutton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 500, 75, 23))
        self.pushButton.setObjectName("pushButton")


    # ------------------------------------------------------------------------------------------------

        self.model = keras.models.load_model('C:/Users/croma/PycharmProjects/GUI/DenseNet121_allfine_5')


        # self.treeView.doubleClicked.connect(self.show_img(self.file_path))
        self.file_path = None
        self.treeView.doubleClicked.connect(self.show_img)
        self.pushButton.clicked.connect(self.btn_function)

    # ------------------------------------------------------------------------------------------------


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open_File"))


    # ------------------------------------------------------------------------------------------------

    def show_img(self, signal):
        file_path = self.treeView.model().filePath(signal)
        self.file_path = file_path
        pixmap = QtGui.QPixmap(self.file_path)
        self.label.setPixmap(pixmap)


    def btn_function(self):
        print(self.file_path)
        S.path = self.file_path
        S.make_name = "aaa.jpeg"

        heatmap, prediction, y_pred = S.Heatmap(self.model, S.path)

        # heatmap_path = S.get_heat_map(heatmap, S.path, S.make_name)
        # pixmap = QtGui.QPixmap(heatmap_path)
        # self.label_2.setPixmap(pixmap)

# ------------------------------------------------------------------------------------------------

class Mytree(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        super(Mytree, self).__init__(parent)
        model = QtWidgets.QFileSystemModel()
        model.setRootPath('C:\\')
        self.setModel(model)
        self.setRootIndex(model.index('C:/Users/croma/Desktop/fold'))
        self.setModel(model)


class Mybutton(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super(Mybutton, self).__init__(parent)


# ------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())