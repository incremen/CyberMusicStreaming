import os
from backend import SERVER_HLS_HOST, SERVER_HLS_PORT, SERVER_CRT_PATH, SERVER_KEY_PATH
from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging
from custom_logging import CustomLogger
from pathlib import Path
import ssl

class HLSHandler(SimpleHTTPRequestHandler):
    def translate_path(self, requested_path):
        try:
            project_root = Path(__file__).resolve().parent.parent
            path_with_spaces = requested_path.replace('%20', ' ')
            return_path = str(project_root) + '/song_segments/' + path_with_spaces
            logging.info(f"Requested path: {path_with_spaces}")
            logging.info(f"project_root: {project_root}")
            logging.info(f"Return path: {return_path}")
            return str(return_path)
        except Exception as e:
            logging.error(f"Error in translate_path: {str(e)}")
            return None

def start_hls_server():
    try:
        logging.info("Starting HLS server..")
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        
        logging.info(f"Loading certificate from: {os.path.abspath(SERVER_CRT_PATH)}")
        logging.info(f"Loading key from: {os.path.abspath(SERVER_KEY_PATH)}")
        context.load_cert_chain(SERVER_CRT_PATH, SERVER_KEY_PATH)
        
        with HTTPServer((SERVER_HLS_HOST, SERVER_HLS_PORT), HLSHandler) as httpd:
            httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
            
            print(f'Serving at https://{SERVER_HLS_HOST}:{SERVER_HLS_PORT}')
            httpd.serve_forever()
    except Exception as e:
        logging.error(f"Error starting HLS server: {str(e)}")
        logging.info("Clearing logs due to error...")
        CustomLogger.clear_logs()
