from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def getAvailableSpot(self,floors,vehicle):
        pass
