from dataclasses import dataclass
from queue import Queue
import math

@dataclass
class SongInfo():
    name: str
    length: float
    nframes: int
    framerate: int
    nchannels : int
    id : int = None
    
    def __repr__(self) -> str:
        return f"SongInfo(name={self.name})"






    