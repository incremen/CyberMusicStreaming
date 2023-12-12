from collections import UserList
from PyQt5.QtCore import pyqtSignal
import logging
import threading


def song_queue_method(func):
    def song_queue_info(song_queue : 'EmittingList', *args, **kwargs):
        logging.debug(f'Before {func.__name__}: {song_queue.data}')
        result = func(song_queue, *args, **kwargs)
        logging.debug(f'After {func.__name__}: {song_queue.data}')
        song_queue.emit_signal()
        return result
    return song_queue_info


class EmittingList(UserList):
    """
    Whenever updated, emits the signal given in __init__ along with the next emit number.
    (events don't always get handled in order so it's necessary to know which emit happened last).
    """
    def __init__(self, signal: pyqtSignal, *args):
        super().__init__(args)
        self.signal = signal
        self.next_emit_num = 0
        
    def emit_signal(self):
        self.signal.emit(self.data, self.next_emit_num) 
        self.next_emit_num += 1
        
    @song_queue_method
    def reset_list(self, new_list : list):
        super().clear()
        super().extend(new_list)
     
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

            
