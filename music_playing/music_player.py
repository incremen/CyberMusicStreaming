import os
import sys
from PyQt5 import QtCore, QtMultimedia
import logging

class MusicPlayer:
    def __init__(self, sound_dir):
        self.player = self.create_player()
        self.sound_dir = sound_dir
        logging.info(os.listdir(sound_dir))
    
    def add_song(self, song_name :str):
        if not song_name.endswith(".mp3"):
            song_name += ".mp3"
        url = QtCore.QUrl.fromLocalFile(os.path.join(self.sound_dir , song_name))
        self.player.setMedia(QtMultimedia.QMediaContent(url))

    def create_player(self):
        player = QtMultimedia.QMediaPlayer()

        def handle_state_changed(state):
            if state == QtMultimedia.QMediaPlayer.PlayingState:
                logging.debug("Started playing")
            elif state == QtMultimedia.QMediaPlayer.StoppedState:
                logging.debug("Finished playing")
                QtCore.QCoreApplication.quit()

        player.stateChanged.connect(handle_state_changed)
        return player

    def play(self):
        self.player.play()

