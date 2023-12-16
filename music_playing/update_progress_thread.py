from PyQt5.QtCore import QThread, QTimer, QEventLoop
from typing import TYPE_CHECKING
import time
import logging
if TYPE_CHECKING:
    from music_playing.audio_handler import AudioHandler


class SongProgressThread(QThread):
    def __init__(self, audio_handler : 'AudioHandler'):
        QThread.__init__(self)
        self.player = audio_handler.player
        self.emitter = audio_handler.main_page_emitter
        self.last_progress = 0
        self.pause = False

    def run(self):
        while True:
            time.sleep(0.3)
            if self.pause:
                continue
            self.update_progress()

    def update_progress(self):
        if not self.player.time_pos:
            return
        current_position = self.player.time_pos
        total_duration = self.player.duration
        progress = int(200 *current_position / total_duration)
        logging.debug(f"{current_position=}, {total_duration=}")
        if progress == self.last_progress:
            return
        logging.debug(f"Emitting {progress=}")
        self.emitter.update_song_progress.emit(progress)
        self.last_progress = progress


