from dataclasses import dataclass


@dataclass
class SongInfo():
    name: str
    length: float
    nframes: int
    framerate: int
    

def return_as_songinfo(song_data_dict):
    if isinstance(song_data_dict, SongInfo):
        return song_data_dict
    if isinstance(song_data_dict, dict):
        return SongInfo(**song_data_dict)
    
    raise TypeError(f"{song_data_dict} is not a SongData or a dict")