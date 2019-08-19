#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\projects\hasher\hasher.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 405)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browse = QtWidgets.QToolButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(650, 40, 111, 31))
        self.browse.setObjectName("browse")
        self.radio_md5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_md5.setGeometry(QtCore.QRect(40, 90, 111, 31))
        self.radio_md5.setChecked(False)
        self.radio_md5.setObjectName("radio_md5")
        self.file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path.setGeometry(QtCore.QRect(40, 40, 551, 31))
        self.file_path.setObjectName("file_path")
        self.radio_sha1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_sha1.setGeometry(QtCore.QRect(160, 90, 111, 31))
        self.radio_sha1.setObjectName("radio_sha1")
        self.radio_sha256 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_sha256.setGeometry(QtCore.QRect(300, 90, 141, 31))
        self.radio_sha256.setChecked(True)
        self.radio_sha256.setObjectName("radio_sha256")
        self.hash = QtWidgets.QPushButton(self.centralwidget)
        self.hash.setGeometry(QtCore.QRect(40, 150, 91, 41))
        self.hash.setObjectName("hash")
        self.hash_result = QtWidgets.QLabel(self.centralwidget)
        self.hash_result.setGeometry(QtCore.QRect(40, 210, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.hash_result.setFont(font)
        self.hash_result.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.hash_result.setFrameShape(QtWidgets.QFrame.Panel)
        self.hash_result.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hash_result.setLineWidth(2)
        self.hash_result.setText("")
        self.hash_result.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.hash_result.setObjectName("hash_result")
        self.compare_value = QtWidgets.QLineEdit(self.centralwidget)
        self.compare_value.setGeometry(QtCore.QRect(40, 260, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.compare_value.setFont(font)
        self.compare_value.setText("")
        self.compare_value.setObjectName("compare_value")
        self.compare = QtWidgets.QPushButton(self.centralwidget)
        self.compare.setGeometry(QtCore.QRect(650, 210, 111, 91))
        self.compare.setObjectName("compare")
        self.match_label = QtWidgets.QLabel(self.centralwidget)
        self.match_label.setGeometry(QtCore.QRect(40, 320, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.match_label.setFont(font)
        self.match_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.match_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.match_label.setLineWidth(2)
        self.match_label.setText("")
        self.match_label.setObjectName("match_label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(140, 152, 451, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Checksum"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.radio_md5.setText(_translate("MainWindow", "MD5"))
        self.file_path.setPlaceholderText(_translate("MainWindow", "Paste or browse to file path"))
        self.radio_sha1.setText(_translate("MainWindow", "SHA1"))
        self.radio_sha256.setText(_translate("MainWindow", "SHA256"))
        self.hash.setText(_translate("MainWindow", "Hash"))
        self.compare_value.setPlaceholderText(_translate("MainWindow", "Paste the checksum value you want to match here."))
        self.compare.setText(_translate("MainWindow", "Compare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

