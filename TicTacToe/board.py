class Board:
    def __init__(self,rows,cols):
        self.board=[[0 for i in range(0,rows)] for j in range(0,cols)]
        self.emptyCells=rows*cols

    def addPlayer(self,row,col,player):
        for i in range(0,len(self.board)):
            for j in range(0,len(self.board[0])):
                if self.board[i][j]==0:
                    self.board[i][j]=player
                    return True
        self.emptyCells-=1
        return False

    def printBoard(self):
        for i in range(0,len(self.board)):
            for j in range(0,len(self.board[0])):
                if (self.board[i][j]==0):
                    print(self.board[i][j])
                else:
                    print(self.board[i][j].playerType)
                print(" | ")
