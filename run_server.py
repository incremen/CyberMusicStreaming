from server.server_socket import ServerSocketHandler
import threading
import os
import custom_logging
from music_playing.convert_to_wav import convert_mp3s_in_directory_to_wav
from server.hls_server import start_hls_server
def main():
    custom_logger = custom_logging.CustomLogger(log_files=["server.log"])
    custom_logger.clear_logs()
    songs_dir = os.path.abspath(r"songs")
    server_thread = threading.Thread(target=start_hls_server)
    server_thread.start()
    
    server_socket_handler = ServerSocketHandler(songs_dir)
    server_socket_handler.start()
    
    

if __name__ == "__main__":
    main()

 