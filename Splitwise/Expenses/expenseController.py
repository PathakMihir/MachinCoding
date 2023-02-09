from typing import List

from Splitwise.Expenses.split import Split
from Splitwise.Splits.splitFactory import SplitFactory
from Splitwise.Expenses.expense import Expense
from Splitwise.BalanceSheet.balanceSheetController import BalanceSheetController
from Splitwise.Users.userController import UserController
from Users.user import User


class ExpenseController:

    def __init__(self):
        self.splitFactory=SplitFactory()
        self.balanceSheetController=BalanceSheetController()
        self.userController=UserController()
        pass

    def addExpense(self,paidBy:User,amount:int,splitList:list[Split],splitType:str):

        split_type=self.splitFactory.createSplitType(splitType)
        if split_type.validateSplit(amount,splitList):
            expense=Expense(paidBy,amount,splitList)

            self.balanceSheetController.addTransaction(paidBy,amount,splitList)
            return expense

        else:
            print("Error in Transaction....")
            return None

