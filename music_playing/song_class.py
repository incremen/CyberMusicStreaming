from dataclasses import dataclass


@dataclass
class SongData():
    name: str
    length: float
    nframes: int
    framerate: int
    

def return_as_songdata(song_data_dict):
    if isinstance(song_data_dict, SongData):
        return song_data_dict
    if isinstance(song_data_dict, dict):
        return SongData(**song_data_dict)
    
    raise TypeError(f"{song_data_dict} is not a SongData or a dict")