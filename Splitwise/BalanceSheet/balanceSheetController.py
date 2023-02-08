from typing import List
from Splitwise.Expenses.split import Split
from Splitwise.Users.user import User

class BalanceSheetController:

    def addTransaction(self,paidBy:User,amount:int,splitList:list[Split]):
        '''

        :param paidBy:
        :param amount:
        :param splitList:
        :return:
        Task:
        1.getPaidBY User and add Expense
        2.Iterate over all Splits:
        3.Add PaidByUser expense
        4.Add OwedUser expense

        '''
        paidByBalancesSheet=paidBy.balanceSheet
        paidByBalancesSheet.totalPayment+=amount

        for split in splitList:
            owedUser=split.user
            amountOwed=split.owedAmount




        pass