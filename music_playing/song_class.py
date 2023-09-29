from dataclasses import dataclass

@dataclass
class SongData():
    name: str
    length: float
    nframes: int
    framerate: int