# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Temp/Subwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        SubWindow.setObjectName("SubWindow")
        SubWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(SubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        SubWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SubWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 21))
        self.menubar.setObjectName("menubar")
        SubWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SubWindow)
        self.statusbar.setObjectName("statusbar")
        SubWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubWindow)
        QtCore.QMetaObject.connectSlotsByName(SubWindow)

        # rows = 4
        # cols = 4
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem("%d" % self.count[i][j]))


        h = self.tableWidget.horizontalHeader()
        h.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        v = self.tableWidget.verticalHeader()
        v.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


    def open(self):
        self.show()


    def retranslateUi(self, SubWindow):
        _translate = QtCore.QCoreApplication.translate
        SubWindow.setWindowTitle(_translate("SubWindow", "MainWindow"))
        self.label_2.setText(_translate("SubWindow", "AI"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("SubWindow", "CNV"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("SubWindow", "DME"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("SubWindow", "DRUSEN"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("SubWindow", "NORMAL"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SubWindow", "CNV"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SubWindow", "DME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SubWindow", "DRUSEN"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SubWindow", "NORMAL"))
        self.label.setText(_translate("SubWindow", "의사"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     SubWindow = QtWidgets.QMainWindow()
#     ui = Ui_SubWindow()
#     ui.setupUi(SubWindow)
#     SubWindow.show()
#     sys.exit(app.exec_())