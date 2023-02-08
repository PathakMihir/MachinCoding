from typing import List

from Splitwise.Expenses.split import Split
from Splitwise.Splits.splitFactory import SplitFactory
from Splitwise.Expenses.expense import Expense
from Splitwise.BalanceSheet.balanceSheetController import BalanceSheetController
from Splitwise.Users.userController import UserController
class ExpenseController:

    def __init__(self):
        self.splitFactory=SplitFactory()
        self.balanceSheetController=BalanceSheetController()
        self.userController=UserController()
        pass

    def addExpense(self,paidBy:int,amount:int,splitList:list[Split],splitType:str):

        split_type=self.splitFactory.createSplitType(splitType)
        if split_type.validateSplit(amount,splitList):
            expense=Expense(paidBy,amount,splitList)
            self.balanceSheetController.addTransaction(self.userController.getUser(paidBy),amount,splitList)
            return expense

        else:
            print("Error in Transaction....")
            return None

