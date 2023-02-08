from abc import abstractmethod,ABC
class SplitType(ABC):

    @abstractmethod
    def validateSplit(self):
        pass

