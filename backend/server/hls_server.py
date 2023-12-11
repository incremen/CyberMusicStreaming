import os
from backend import HLS_HOST, HLS_PORT
from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging
from custom_logging import CustomLogger
from pathlib import Path


class HLSHandler(SimpleHTTPRequestHandler):
    def translate_path(self, requested_path):
        segments_dir = Path('song_segments')
        return_path = segments_dir / Path(requested_path).relative_to('/')
        abs_return_path = return_path.absolute()
        logging.info(f"Requested path: {requested_path}")
        logging.debug(f"Return path: {abs_return_path}")
        logging.debug(f"Return path exists: {abs_return_path.exists()}")
        return str(abs_return_path)


def start_hls_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with HTTPServer((HLS_HOST, HLS_PORT), HLSHandler) as httpd:
        print(f'Serving at http://{HLS_HOST}:{HLS_PORT}')
        httpd.serve_forever()