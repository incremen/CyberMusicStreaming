import os

DB_PATH = r"D:\vs_code_projects_good_place\cyber_music_streaming\database\test_db.db"
SQLITE_PATH = fr"sqlite:///{DB_PATH}?check_same_thread=False"
SONG_DIR = os.path.abspath(r"songs")
