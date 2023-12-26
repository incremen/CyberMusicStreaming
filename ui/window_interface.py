from abc import ABC, abstractmethod

class WindowInterface(ABC):
    @abstractmethod
    def start(self):
        pass
