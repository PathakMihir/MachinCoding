from typing import Optional, Any

from .user import User


class UserController:

    def __init__(self):
        self.userList = []

    def addUser(self, user: User) -> None:
        self.userList.append(user)


    def getUser(self, name) -> Optional[Any]:

        for user in self.userList:
            if user.name == name:
                return user
        return None
