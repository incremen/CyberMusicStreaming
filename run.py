from music_playing.audio_handler import AudioHandler
from backend.client_socket import ClientSocketHandler
from backend.server_socket import ServerSocketHandler
import threading
import os
import custom_logging
from music_playing.convert_to_wav import convert_mp3s_in_directory_to_wav

def main():
    custom_logger = custom_logging.CustomLogger()
    client_socket_handler = ClientSocketHandler()

    songs_dir = os.path.abspath(r"songs")
    
    server_socket_handler = ServerSocketHandler(songs_dir)
    server_thread = threading.Thread(target=server_socket_handler.start)
    server_thread.start()
    
    client_socket_handler.connect()
    client_socket_handler.request_song("cant_keep_getting_away")
    client_socket_handler.request_song("american")
    

if __name__ == "__main__":
    main()

