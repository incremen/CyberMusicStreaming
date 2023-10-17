from dataclasses import dataclass
from queue import Queue
import math

@dataclass
class SongToSend():
    name: str
    order: int


@dataclass
class SongInfo():
    name: str
    length: float
    nframes: int
    framerate: int
    nchannels : int
    max_seq : int
    
    def __repr__(self) -> str:
        return f"SongInfo(name={self.name},max_seq={self.max_seq})"
    

@dataclass
class SongChunk():
    chunk : bytes
    name : str
    order : int
    seq : int
    
    def __repr__(self) -> str:
        return f"SongChunk(name={self.name},order={self.order},seq={self.seq})"


class SongBuffer(dict):
    def __init__(self, info :SongInfo, order : int):
        super().__init__()
        self.info = info
        self.order = order
        
    def __repr__(self) -> str:
        return f"SongBuffer({self.info.name},{self.info.max_seq}, order={self.order})"





    