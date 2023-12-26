from abc import ABC, abstractmethod, ABCMeta
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow


pyqtWrapperType = type(QtCore.QObject)


class CombinedMeta(pyqtWrapperType, ABCMeta):
    pass


class WindowInterface(ABC, metaclass=CombinedMeta):
    @abstractmethod
    def start(self):
        pass
    
    # @abstractmethod
    # def hide(self):
    #     pass




