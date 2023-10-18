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
        
        
    def clear_until_order(self, order : int):
        """
        Clear all songs in the list with an order less than the order given.

        Parameters:
            order (int): The order until which the songs should be cleared.

        Returns:
            None
        """
        songs_to_remove = [song for song in self.data if song.order < order]
        for song in songs_to_remove:
            super().remove(song)
            
        self.emit_signal()
        
    def clear_range(self, start : int, end : int):
        """
        Remove a range of elements from the list.

        Parameters:
            start (int): The starting index (inclusive) of the range to be removed.
            end (int): The ending index (exclusive) of the range to be removed.

        Returns:
            None
        """
        
        
        if start < 0:
            raise IndexError("Start index less than 0")
        
        if end > len(self):
            raise IndexError("End index greater than list length")
        
        if start > end:
            raise IndexError("Start index greater than end index")
        
        del self.data[start:end]
        self.emit_signal()
