from abc import abstractmethod,ABC
class WeightMachineAdaptor(ABC):

    @abstractmethod
    def getWeightInKg(self):
        pass