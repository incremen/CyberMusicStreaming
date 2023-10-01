from dataclasses import dataclass


@dataclass
class SongInfo():
    name: str
    length: float
    nframes: int
    framerate: int
    nchannels : int
    

def return_as_songinfo(song_info_dict, **kwargs) -> SongInfo:
    if song_info_dict is None:
        return SongInfo(**kwargs)
    if isinstance(song_info_dict, SongInfo):
        return song_info_dict
    if isinstance(song_info_dict, dict):
        return SongInfo(**song_info_dict)
    
    raise TypeError(f"{song_info_dict} is not a SongInfo or a dict")