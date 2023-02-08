from typing import Optional, Any

from .group import Group


class GroupController:

    def __init__(self):
        self.groupList = []

    def addGroup(self, group: Group) -> None:
        self.groupList.append(group)

    def getGroup(self, name: str) -> Optional[Any]:

        for group in self.groupList:
            if group.name == name:
                return group
        return None
