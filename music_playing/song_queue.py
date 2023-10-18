from collections import UserList
from PyQt5.QtCore import pyqtSignal

class SongQueue(UserList):
    def __init__(self, signal: pyqtSignal, *args):
        super().__init__(args)
        self.signal = signal
    
    def emit_signal(self):
        self.signal.emit(self.data) 
     
    def append(self, item):
        super().append(item)
        self.emit_signal()
    
    def extend(self, iterable):
        super().extend(iterable)
        self.emit_signal()
    
    def insert(self, i, item):
        super().insert(i, item)
        self.emit_signal()
    
    def remove(self, item):
        super().remove(item)
        self.emit_signal()
    
    def pop(self, i=-1):
        result = super().pop(i)
        self.emit_signal()
        return result
    
    def clear(self):
        super().clear()
        self.emit_signal()
    
    def __setitem__(self, i, item):
        super().__setitem__(i, item)
        self.emit_signal()
        
    def clear_range(self, start, end):
        if start < 0:
            raise IndexError("Start index less than 0")
        
        if end > len(self):
            raise IndexError("End index greater than list length")
        
        if start > end:
            raise IndexError("Start index greater than end index")
        
        del self.data[start:end]
        self.emit_signal()
