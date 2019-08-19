#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog 
from Ui_hasher import *

from hashlib import sha256, md5, sha1
from os.path import getsize


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super().__init__(parent)
        self.setupUi(self)
        self.browse.clicked.connect(self.browsefile)
        self.hash.clicked.connect(self.output_checksum)
        self.compare.clicked.connect(self.compare_function)
    
    def browsefile(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Choose File to Hash","./")
        if filepath:
            self.file_path.setText(filepath)
        # self.file_path is the QLineEdit object
    
    def checksum(self, filename, hasher, block_size=65536):
        percent_step = 100 * block_size / getsize(filename)
        percent=0
        with open(filename, 'rb') as f:
            for block in iter(lambda: f.read(block_size), bytearray()):
                hasher.update(block)
                percent = percent + percent_step
                self.progressBar.setValue(percent)
        self.progressBar.setValue(100)
        return hasher.hexdigest()
    
    def output_checksum(self):
        hasher = sha256()
        if self.radio_md5.isChecked()==True:
            hasher=md5()
        elif self.radio_sha1.isChecked()==True:
            hasher=sha1()
        try:    
            result=self.checksum(self.file_path.text(), hasher)
            self.hash_result.setText(result)
        except:
            pass
        
        #self.hash_result.adjustSize()
    
    def compare_function(self):
        if self.hash_result.text()==self.compare_value.text():
            self.match_label.setText("Matched!")
        else:
            self.match_label.setText("unmatched:(")
        self.match_label.adjustSize()
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_()) 
