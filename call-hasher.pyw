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
        hasher = sha256()
        if self.radio_md5.isChecked()==True:
            hasher=md5()
        elif self.radio_sha1.isChecked()==True:
            hasher=sha1()
        try:    
            result=self.checksum(self.file_path.text(), hasher)
            self.hash_result.setText(result)
        except:
            QMessageBox.about(self, "Error", "No such file. Please check the path")
        
        #self.hash_result.adjustSize()
    
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

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()    

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress        

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
        


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
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)

if __name__=="__main__":
    from os import environ
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv) 
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_()) 
