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
        self.data.clear()
        self.emit_signal()
    
    def __setitem__(self, i, item):
        super().__setitem__(i, item)
        self.emit_signal()
    
    def clear_range(self, start, end):
        if start < 0:
            raise IndexError("start is less than 0")
        if end >= len(self):
            raise IndexError("end is greater than or equal to the length of the list")
        
        for i in range(start, end+1):
            super().pop(i)
        
        self.emit_signal()

