from collections import UserList
from PyQt5.QtCore import pyqtSignal
import logging
import threading


def emitting_list_method(func):
    def update_and_emit(song_queue : 'EmittingList', *args, **kwargs):
        # logging.debug(f'Before {func.__name__}: {song_queue.data}')
        result = func(song_queue, *args, **kwargs)
        # logging.debug(f'After {func.__name__}: {song_queue.data}')
        song_queue.emit_signal()
        return result
    return update_and_emit


class EmittingList(UserList):
    """
    Whenever updated, emits the signal given in __init__ along with the next emit number.
    (events don't always get handled in order so it's necessary to know which emit happened last).
    Doesn't appear to support list slicing for some reason?
    """
    def __init__(self, signal: pyqtSignal, *args):
        super().__init__(args)
        self.signal = signal
        self.next_emit_num = 0
        
    def emit_signal(self):
        self.signal.emit(self.data, self.next_emit_num) 
        self.next_emit_num += 1
        
    @emitting_list_method
    def reset_list(self, new_list : list):
        super().clear()
        super().extend(new_list)
     
    @emitting_list_method
    def append(self, item):
        super().append(item)
    
    @emitting_list_method
    def extend(self, iterable):
        super().extend(iterable)
    
    @emitting_list_method
    def insert(self, i, item):
        super().insert(i, item)
    
    @emitting_list_method
    def remove(self, item):
        super().remove(item)
    
    @emitting_list_method
    def pop(self, i=-1):
        result = super().pop(i)
        return result
    
    @emitting_list_method
    def clear(self):
        super().clear()
    
    @emitting_list_method
    def __setitem__(self, i, item):
        super().__setitem__(i, item)
        
    def __getitem__(self, i):
        res = self.data[i]
        return type(self)(res) if isinstance(i, slice) else res

            
