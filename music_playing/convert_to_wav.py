import os
from pydub import AudioSegment
import logging


def convert_mp3s_in_directory_to_wav(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            convert_mp3_to_wav(directory, filename)
            
    logging.info(f"Converted all .mp3s in {directory}")


def convert_mp3_to_wav(directory, filename):
    mp3_path = os.path.join(directory, filename)
    logging.debug(f"{mp3_path=}")
    audio = AudioSegment.from_mp3(mp3_path)
    wav_path = mp3_path.replace('.mp3', '.wav')
    audio.export(wav_path, format="wav")
    logging.info(f"Converted {mp3_path} to {wav_path}")

