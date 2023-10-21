from collections import UserList
from PyQt5.QtCore import pyqtSignal
import logging


def log_change(func):
    def song_queue_info(self : 'SongQueue', *args, **kwargs):
        logging.debug(f'Before {func.__name__}: {self.data}')
        result = func(self, *args, **kwargs)
        logging.debug(f'After {func.__name__}: {self.data}')
        return result
    return song_queue_info


class SongQueue(UserList):
    def __init__(self, signal: pyqtSignal, *args):
        super().__init__(args)
        self.signal = signal
        
    def emit_signal(self):
        self.signal.emit(self.data) 
     
    @log_change
    def append(self, item):
        super().append(item)
        self.emit_signal()
    
    @log_change
    def extend(self, iterable):
        super().extend(iterable)
        self.emit_signal()
    
    @log_change
    def insert(self, i, item):
        super().insert(i, item)
        self.emit_signal()
    
    @log_change
    def remove(self, item):
        super().remove(item)
        self.emit_signal()
    
    @log_change
    def pop(self, i=-1):
        result = super().pop(i)
        self.emit_signal()
        return result
    
    @log_change
    def clear(self):
        super().clear()
        self.emit_signal()
    
    @log_change
    def __setitem__(self, i, item):
        super().__setitem__(i, item)
        self.emit_signal()
        
        
    @log_change
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
