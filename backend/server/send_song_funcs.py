CHUNK = 4096
from dataclasses import asdict
import logging
import wave

def send_song_data(sio, song_name, sid, wf):
    print("Sending song data...")
    while True:
            if skip_song_flag:
                skip_song_flag = False
                return
            
            song_data = wf.readframes(CHUNK)
            if not song_data:
                return
            logging.debug("About to send a packet")
            sio.emit('audio_data', (song_data, song_name), room=sid)
            logging.debug("Packet sent")