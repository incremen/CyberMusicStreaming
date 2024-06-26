import os
from backend import SERVER_HLS_HOST, SERVER_HLS_PORT, SERVER_CRT_PATH, SERVER_KEY_PATH
from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging
from custom_logging import CustomLogger
from pathlib import Path
import ssl

class HLSHandler(SimpleHTTPRequestHandler):
    def translate_path(self, requested_path):
        path_with_spaces = requested_path.replace('%20', ' ')
        segments_dir = Path(r'D:\vs_code_projects_good_place\cyber_music_streaming\song_segments')
        return_path = segments_dir / Path(path_with_spaces).relative_to('/')
        abs_return_path = return_path.absolute()
        logging.info(f"Requested path: {path_with_spaces}")
        logging.debug(f"Return path: {abs_return_path}")
        logging.debug(f"Return path exists: {abs_return_path.exists()}")
        return str(abs_return_path)


def start_hls_server():
    logging.info("Starting HLS server..")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    
    context.load_cert_chain(SERVER_CRT_PATH, SERVER_KEY_PATH)
    
    with HTTPServer((SERVER_HLS_HOST, SERVER_HLS_PORT), HLSHandler) as httpd:
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        
        print(f'Serving at https://{SERVER_HLS_HOST}:{SERVER_HLS_PORT}')
        httpd.serve_forever()