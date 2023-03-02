class UserController():

    def __init__(self):
        self.users = []

    def addUser(self, user):
        self.users.append(user)

    def getUser(self, name):
        return self.users[0]
