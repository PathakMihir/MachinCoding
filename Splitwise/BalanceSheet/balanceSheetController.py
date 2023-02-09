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


            owedUser.balanceSheet.totalExpense+=split.owedAmount

            if owedUser.id!=paidBy.id:
                owedUser.balanceSheet.owedMoney+=split.owedAmount
                #add in paidUser Balance sheet
                if owedUser not in paidByBalancesSheet.friends:
                    paidByBalancesSheet.friends[owedUser]=0
                paidByBalancesSheet.friends[owedUser]+=amountOwed
                paidByBalancesSheet.getMoney+=amountOwed


                #add in owedUser Balancesheet
                if paidBy not in owedUser.balanceSheet.friends:
                    owedUser.balanceSheet.friends[paidBy]=0
                owedUser.balanceSheet.friends[paidBy]-=amountOwed

    def showBalance(self,user:User):

        print("----------------------------------------")
        print("BalanceSheet of User: "+ user.name+"\n")
        print("Total Expense: "+str(user.balanceSheet.totalExpense))
        print("Total Payment: "+str(user.balanceSheet.totalPayment))
        print("Total Get Money: "+str(user.balanceSheet.getMoney))
        print("Total Owed Money: "+str(user.balanceSheet.owedMoney))
        print("----------------------------------------")
