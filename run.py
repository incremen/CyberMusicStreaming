from music_playing.audio_handler import AudioHandler
from backend.client_socket import ClientSocketHandler
from backend.server_socket import ServerSocket
import threading
import os
import custom_logging
import time
import eventlet

def main():
    eventlet.monkey_patch()
    
    custom_logger = custom_logging.CustomLogger()
    audio_handler = AudioHandler()
    client_socket_handler = ClientSocketHandler(audio_handler)

    song_path = os.path.abspath(r"sounds\cant_keep_getting_away.wav")
    
    server_socket = ServerSocket(song_path)
    server_thread = threading.Thread(target=server_socket.start)
    server_thread.start()
    time.sleep(0.3)
    client_socket_handler.connect()

if __name__ == "__main__":
    main()

