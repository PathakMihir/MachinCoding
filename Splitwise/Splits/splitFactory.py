from Splitwise.Splits.percentageSplit import PersentageSplit
from Splitwise.Splits.equalSplit import EqualSplit
from Splitwise.Splits.unequalSplit import UnequalSplit


class SplitFactory:

    def createSplitType(self, name: str):

        if name == "EQUAL":
            return EqualSplit()
        elif name == "PERCENTAGE":
            return PersentageSplit()
        elif name == "UNEQUAL":
            return UnequalSplit()
        else:
            raise NotImplementedError()
