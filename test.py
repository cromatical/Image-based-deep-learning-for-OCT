# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import QDate, Qt
#
# class MainApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("SAINT_Medical_AI")
#         self.setGeometry(50, 50, 600, 600)
#         self.date = QDate.currentDate()
#         self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
#
#         openFile = QAction("Open_File", self)
#         openFile.triggered.connect(self.file_open())
#
#         close_Action = QAction("Close", self)
#         close_Action.triggered.connect(self.close_application)
#
#         self.statusBar()
#
#         mainMenu = self.menuBar()
#         fileMenu = mainMenu.addMenu('&File')
#         fileMenu.addAction(close_Action)
#         fileMenu.addAction(openFile)
#
#
#         self.tabimage = TabImage()
#         self.setCentralWidget(self.tabimage)
#         self.show()
#
#
#     def file_open(self):
#         name = QFileDialog.getOpenFileName(self, 'Open File')
#         file = open(name, 'r')
#
#         self.editor()
#
#         with file:
#             text = file.read()
#             self.textEdit.setText(text)
#
#     def close_application(self):
#         choice = QMessageBox.question(self, 'Extract!',
#                                             "Get into the chopper?",
#                                             QMessageBox.Yes | QMessageBox.No)
#         if choice == QMessageBox.Yes:
#             print("Extracting Naaaaaaoooww!!!!")
#             sys.exit()
#         else:
#             pass
#
#


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate, Qt

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("SAINT_Medical_AI")
        self.setGeometry(50, 50, 600, 600)

        self.date = QDate.currentDate()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        editMenu = menubar.addMenu('Edit')
        self.resize(500, 500)

        openAction = QAction('Open Image', self)
        openAction.triggered.connect(self.openImage)
        fileMenu.addAction(openAction)

        closeAction = QAction('Exit', self)
        closeAction.triggered.connect(self.close)
        fileMenu.addAction(closeAction)
        self.label = QLabel()
        self.setCentralWidget(self.label)

        self.tabimage = TabImage()
        self.setCentralWidget(self.tabimage)

    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(pixmap)
        self.resize(pixmap.size())
        self.adjustSize()

class TabImage(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.container = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tab1_layout = QVBoxLayout()
        self.tab2_layout = QVBoxLayout()
        self.tab3_layout = QVBoxLayout()

        self.tab1.setLayout(self.tab1_layout)
        self.tab2.setLayout(self.tab2_layout)
        self.tab3.setLayout(self.tab3_layout)

        self.tab1_label = QLabel()
        self.tab2_label = QLabel()
        self.tab3_label = QLabel()

        self.tab1_pixMap = QPixmap("C:/Users/user/Desktop/aaa.PNG")
        self.tab2_pixMap = QPixmap("C:/Users/user/Desktop/aaa.PNG")
        self.tab3_pixMap = QPixmap("C:/Users/user/Desktop/aaa.PNG")

        self.tab1_label.setPixmap(self.tab1_pixMap)
        self.tab2_label.setPixmap(self.tab2_pixMap)
        self.tab3_label.setPixmap(self.tab3_pixMap)

        self.tab1_layout.addWidget(self.tab1_label)
        self.tab2_layout.addWidget(self.tab2_label)
        self.tab3_layout.addWidget(self.tab3_label)

        self.tabs.addTab(self.tab1, "Original_Image")
        self.tabs.addTab(self.tab2, "Crop_Image")
        self.tabs.addTab(self.tab3, "HeatMap")
        self.container.addWidget(self.tabs)

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())