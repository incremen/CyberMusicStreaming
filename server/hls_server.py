import os
from backend import SERVER_HLS_HOST, SERVER_HLS_PORT
from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging
from custom_logging import CustomLogger
from pathlib import Path


class HLSHandler(SimpleHTTPRequestHandler):
    def translate_path(self, requested_path):
        segments_dir = Path(r'D:\vs_code_projects_good_place\cyber_music_streaming\song_segments')
        return_path = segments_dir / Path(requested_path).relative_to('/')
        abs_return_path = return_path.absolute()
        logging.info(f"Requested path: {requested_path}")
        logging.debug(f"Return path: {abs_return_path}")
        logging.debug(f"Return path exists: {abs_return_path.exists()}")
        return str(abs_return_path)


def start_hls_server():
    logging.info("Starting HLS server..")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with HTTPServer((SERVER_HLS_HOST, SERVER_HLS_PORT), HLSHandler) as httpd:
        print(f'Serving at http://{SERVER_HLS_HOST}:{SERVER_HLS_PORT}')
        httpd.serve_forever()