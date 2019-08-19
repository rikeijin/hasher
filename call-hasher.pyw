#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
# from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox 
from Ui_hasher import *
import traceback, sys

from hashlib import sha256, md5, sha1
from os.path import getsize

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super().__init__(parent)
        self.setupUi(self)
        self.browse.clicked.connect(self.browsefile)
        self.hash.clicked.connect(self.output_checksum)
        self.compare.clicked.connect(self.compare_function)
        self.threadpool = QThreadPool()
    
    def browsefile(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Choose File to Hash","./")
        if filepath:
            self.file_path.setText(filepath)
        # self.file_path is the QLineEdit object
    
    def checksum(self, filename, hasher, block_size=65536):
        percent_step = 100 * block_size / getsize(filename)
        percent=0
        # open file with 'r'=read mode and 'b'=byte mode
        with open(filename, 'rb') as f:
            # read file until an sentinel bytearray()=""
            # lambda: f.read(block_size) is a function without input varaible
            for block in iter(lambda: f.read(block_size), bytearray()):
                hasher.update(block)
                percent = percent + percent_step
                self.progressBar.setValue(percent)
        self.progressBar.setValue(100)
        return hasher.hexdigest()
    
    def output_checksum(self):
        block_size=65536
        path_and_filename = self.file_path.text()
        hasher = sha256()
        if self.radio_md5.isChecked()==True:
            hasher=md5()
        elif self.radio_sha1.isChecked()==True:
            hasher=sha1()
        worker=Worker(path_and_filename, hasher, block_size)
        worker.signals.error.connect(self.pop_error_window)
        worker.signals.result.connect(self.show_checksum)
        worker.signals.progress.connect(self.update_progress)
        self.threadpool.start(worker)
    def pop_error_window(self):
        QMessageBox.about(self, "Error", "No such file. Please check the path")
    def show_checksum(self, checksum):
        self.hash_result.setText(checksum)
    def update_progress(self, p):
        self.progressBar.setValue(p)
        
    
    def compare_function(self):
        if self.hash_result.text()==self.compare_value.text():
            self.match_label.setText("Matched!")
        else:
            self.match_label.setText("Unmatched:(")
        self.match_label.adjustSize()
        
        
class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, filename, hasher, blocksize):
        super(Worker, self).__init__()
        self.filename=filename
        self.hasher=hasher
        self.block_size=blocksize
        self.signals = WorkerSignals()        
        
    @pyqtSlot()
    def run(self):
        try:
            percent_step = 100 * self.block_size / getsize(self.filename)
            percent=0
            with open(self.filename, 'rb') as f:
                for block in iter(lambda: f.read(self.block_size), bytearray()):
                    self.hasher.update(block)
                    percent = percent + percent_step
                    self.signals.progress.emit(int(percent))
            self.signals.progress.emit(100)
            self.signals.result.emit(self.hasher.hexdigest())
        except:
            self.signals.error.emit()
#        finally:
#            self.signals.finished.emit()
        


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything
        
    Defines the signals available from a running worker thread.

    progress
        int progress complete,from 0-100

    '''
    progress = pyqtSignal(int)
#    finished = pyqtSignal()
    error = pyqtSignal()
    result = pyqtSignal(str)

if __name__=="__main__":
    from os import environ
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv) 
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_()) 
