from dataclasses import dataclass

from music_playing.song_class import SongData

song_info_dict = {
    "name": "My Song",
    "length": 180.5,
    "nframes": 44100,
    "framerate": 44100
}

# Create a SongData object from the dictionary
song_data = SongData(**song_info_dict)

print(song_data)