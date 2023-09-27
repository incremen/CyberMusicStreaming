import os
import sys
from PyQt5 import QtCore, QtMultimedia
import logging
from music_playing.music_player import MusicPlayer


def main():
    app = QtCore.QCoreApplication([])
    sound_dir = os.path.abspath("sounds")
    player = MusicPlayer(sound_dir)
    player.add_song("cant_keep_getting_away")
    player.play()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
