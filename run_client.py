from backend.client.client_socket import ClientSocketHandler
import custom_logging
from PyQt5.QtWidgets import QApplication
import sys


def main():
    custom_logger = custom_logging.CustomLogger(log_files=["client.log"])
    app = QApplication(sys.argv)
    
    client_socket_handler = ClientSocketHandler()
    
    client_socket_handler.connect()
    client_socket_handler.emit_to_server("song_list_request")

    app.exec_()
    
if __name__ == "__main__":
    main()

