from collections import UserList
from PyQt5.QtCore import pyqtSignal
import logging
import threading

def song_queue_method(func):
    def song_queue_info(song_queue : 'EmittingSongList', *args, **kwargs):
        with song_queue.lock:
            logging.debug(f'Before {func.__name__}: {song_queue.data}')
            result = func(song_queue, *args, **kwargs)
            logging.debug(f'After {func.__name__}: {song_queue.data}')
            song_queue.emit_signal()
            
        return result
    return song_queue_info


class EmittingSongList(UserList):
    """
    Whenever updated, emits the signal given in __init__.

    """
    def __init__(self, signal: pyqtSignal, *args):
        super().__init__(args)
        self.signal = signal
        self.lock = threading.Lock()
        self.next_emit_num = 0
        
    def emit_signal(self):
        self.signal.emit(self.data, self.next_emit_num) 
        self.next_emit_num += 1
     
    @song_queue_method
    def append(self, item):
        super().append(item)
    
    @song_queue_method
    def extend(self, iterable):
        super().extend(iterable)
    
    @song_queue_method
    def insert(self, i, item):
        super().insert(i, item)
    
    @song_queue_method
    def remove(self, item):
        super().remove(item)
    
    @song_queue_method
    def pop(self, i=-1):
        result = super().pop(i)
        return result
    
    @song_queue_method
    def clear(self):
        super().clear()
    
    @song_queue_method
    def __setitem__(self, i, item):
        super().__setitem__(i, item)
        
        
    @song_queue_method
    def clear_until_order(self, order : int):
        """
        Clear all songs in the list with an order less than the order given.

        Parameters:
            order (int): The order until which the songs should be cleared.
        """
        songs_to_remove = [song for song in self.data if song.order < order]
        for song in songs_to_remove:
            super().remove(song)
            
