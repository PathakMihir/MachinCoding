from Splitwise.Expenses.expenseController import ExpenseController
from Splitwise.Users.userController import UserController
from Splitwise.Users.user import User
from Splitwise.Expenses.split import Split


class Splitwise:

    def __init__(self):
        self.expenseController = ExpenseController()
        self.userController=self.expenseController.userController

    def addUsers(self):
        self.userController.addUser(User("U1"))
        self.userController.addUser(User("U2"))
        self.userController.addUser(User("U3"))

    def demo(self):
        self.addUsers()
        # 1.PaidBy
        user1 = self.userController.getUser("U1")
        user2 = self.userController.getUser("U2")
        user3 = self.userController.getUser("U3")
        print(user1)
        # 2.CreateSplits
        splitList = []
        splitList.append(Split(user1, 300))
        splitList.append(Split(user2, 300))
        splitList.append(Split(user3, 300))

        self.expenseController.addExpense(user1, 900, splitList, "EQUAL")

        for user in self.userController.userList:
            self.expenseController.balanceSheetController.showBalance(user)


if __name__ == "__main__":
    app = Splitwise()
    app.demo()
