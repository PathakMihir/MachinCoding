from Splitwise.BalanceSheet.balanceSheet import BalanceSheet
class User():
    _id=1
    def __init__(self,name):
        self.id=User._id
        self.name=name
        self.balanceSheet=BalanceSheet()
        User._id+=1


