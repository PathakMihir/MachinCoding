from typing import List

from Splitwise.Users.user import User
from Splitwise.Expenses.split import Split


class Expense:

    def __init__(self, paidBy: User, amount: int, splitsList: List[Split]):
        """

        :param paidBy:
        :param amount:
        :param splitsList:
        """
        self.paidBy = paidBy
        self.amount = amount
        self.splits = splitsList
