from Splitwise.Splits.splitType import SplitType
class EqualSplit(SplitType):

    def validateSplit(self,amount,splits):
        amount_per_user=amount//len(splits)
        for split in splits:
            if split.owedAmount!=amount_per_user:
                return False
        return True
