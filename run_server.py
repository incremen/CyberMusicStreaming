from backend.server.server_socket import ServerSocketHandler
import threading
import os
import custom_logging
from music_playing.convert_to_wav import convert_mp3s_in_directory_to_wav
from backend.server.hls_server import start_hls_server
def main():
    custom_logger = custom_logging.CustomLogger(log_files=["server.log"])
    custom_logger.clear_logs()
    songs_dir = os.path.abspath(r"songs")
    
    server_socket_handler = ServerSocketHandler()
    server_socket_handler.start()
    
    start_hls_server()
    

if __name__ == "__main__":
    main()

 