from dataclasses import dataclass
from queue import Queue
import math
from database.models import Song
@dataclass
class SongInfo():
    name: str
    length: float
    nframes: int
    framerate: int
    nchannels : int
    id : int
    
    def __repr__(self) -> str:
        return f"SongInfo(name={self.name})"



def song_orm_to_songinfo(song: Song):
    return SongInfo(**song.as_dict())

    