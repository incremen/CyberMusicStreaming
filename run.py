from music_playing.audio_handler import AudioHandler
from backend.client_socket import ClientSocketHandler
from backend.server_socket import ServerSocketHandler
import threading
import os
import custom_logging

def main():
    custom_logger = custom_logging.CustomLogger()
    client_socket_handler = ClientSocketHandler()

    song_path = os.path.abspath(r"sounds\cant_keep_getting_away.wav")
    
    server_socket_handler = ServerSocketHandler(song_path)
    server_thread = threading.Thread(target=server_socket_handler.start)
    server_thread.start()
    
    client_socket_handler.connect()
    client_socket_handler.request_song(song_path)

if __name__ == "__main__":
    main()

