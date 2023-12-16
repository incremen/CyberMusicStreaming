import wave
import math
import os
from custom_logging import CustomLogger
import logging
from pydub import AudioSegment

testing_logger = CustomLogger(log_files=["testing.log"])
from collections import UserList
CHUNK = 4096


class EmittingList(UserList):
    def __init__(self, *args):
        super().__init__(args)
        
my_list = EmittingList(1,2,3,4,5)
logging.debug(f"{my_list=}, {my_list[2:]=}")
