import os
import sys
from PyQt5 import QtCore, QtMultimedia
import custom_logging


custom_logger = custom_logging.CustomLogger()

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
app = QtCore.QCoreApplication(sys.argv)
