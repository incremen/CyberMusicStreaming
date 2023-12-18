import wave
import math
import os
from custom_logging import CustomLogger
import logging
from pydub import AudioSegment

testing_logger = CustomLogger(log_files=["testing.log"])
import mpv

player = mpv.MPV()
player.play('songs/cant_keep_getting_away.wav')
player.wait_for_playback()

logging.debug(f"{player.time_pos=}")
