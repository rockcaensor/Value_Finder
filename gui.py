# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searcher.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 200))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.widget.setObjectName("widget")
        self.BrowseButton = QtWidgets.QPushButton(self.widget)
        self.BrowseButton.setGeometry(QtCore.QRect(9, 74, 75, 23))
        self.BrowseButton.setObjectName("BrowseButton")
        self.FolderView = QtWidgets.QListWidget(self.widget)
        self.FolderView.setGeometry(QtCore.QRect(9, 9, 755, 59))
        self.FolderView.setObjectName("FolderView")
        self.SearchButton = QtWidgets.QPushButton(self.widget)
        self.SearchButton.setGeometry(QtCore.QRect(9, 168, 75, 23))
        self.SearchButton.setObjectName("SearchButton")
        self.SearchInput = QtWidgets.QTextEdit(self.widget)
        self.SearchInput.setGeometry(QtCore.QRect(10, 130, 751, 31))
        self.SearchInput.setObjectName("SearchInput")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LogWindow = QtWidgets.QListWidget(self.widget_2)
        self.LogWindow.setMinimumSize(QtCore.QSize(760, 0))
        self.LogWindow.setObjectName("LogWindow")
        self.verticalLayout_2.addWidget(self.LogWindow)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	ex = Ui_MainWindow()
	ex.setupUi()
	sys.exit(app.exec_())
	