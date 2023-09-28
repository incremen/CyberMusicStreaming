from backend.client.client_socket import ClientSocketHandler
import custom_logging
from PyQt5.QtWidgets import QApplication
from frontend.main_page import MainPage
import sys


def main():
    custom_logger = custom_logging.CustomLogger(log_files=["client.log"])
    app = QApplication(sys.argv)
    main_page = MainPage()
    song_list=[{'name': 'american.wav'}, {'name': 'cant_keep_getting_away.wav'},
               {'name': 'cvar_lo_koev.wav'}, {'name': 'No_38.wav'}, {'name': 'No_39.wav'},
               {'name': 'No_40.wav'}, {'name': 'No_41.wav'}, {'name': 'No_42.wav'},]
    main_page.song_list_received(song_list)
    
    # client_socket_handler = ClientSocketHandler()
    
    # client_socket_handler.connect()
    # client_socket_handler.emit_to_server("song_list_request")

    app.exec_()
    
if __name__ == "__main__":
    main()

