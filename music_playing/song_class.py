from dataclasses import dataclass
from queue import Queue
import math

@dataclass
class SongToSend():
    name: str
    id: int


@dataclass
class SongInfo():
    name: str
    length: float
    nframes: int
    framerate: int
    nchannels : int
    max_seq : int
    id : int = None
    
    def __repr__(self) -> str:
        return f"SongInfo(name={self.name},max_seq={self.max_seq},id={self.id})"
    

@dataclass
class SongChunk():
    chunk : bytes
    name : str
    id : int
    seq : int
    
    def __repr__(self) -> str:
        return f"SongChunk(name={self.name},id={self.id},seq={self.seq})"


class SongBuffer(dict):
    def __init__(self, info :SongInfo):
        super().__init__()
        self.info = info
        
    def __repr__(self) -> str:
        return f"SongBuffer(of ({self.info})"





    