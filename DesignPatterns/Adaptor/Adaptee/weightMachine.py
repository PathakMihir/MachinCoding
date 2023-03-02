from abc import abstractmethod, ABC


class WeightMachine(ABC):

    @abstractmethod
    def getWeightInPound(self):
        pass
