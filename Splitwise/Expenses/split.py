from Splitwise.Users.user import User

class Split:

    def __init__(self,user:User,owedAmount:int):
        self.user=user
        self.owedAmount=owedAmount

