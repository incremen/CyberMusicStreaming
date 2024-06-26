import os

import os
import sys

# Get the root directory of the main process
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, use the sys._MEIPASS
    root_dir = sys._MEIPASS
else:
    # If the application is run from a script, use the script's directory
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(root_dir, "database", "test_db.db")
SQLITE_PATH = fr"sqlite:///{DB_PATH}?check_same_thread=False"
SONG_DIR = os.path.abspath(r"songs")
