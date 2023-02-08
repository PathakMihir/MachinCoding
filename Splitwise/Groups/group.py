class Group:
    _id=1
    def __init__(self,name: str):
        self.id=Group._id
        self.name=name
        self.users=[]
        self.totalExpense=0
        Group._id+=1

    def createExpense(self):
        pass