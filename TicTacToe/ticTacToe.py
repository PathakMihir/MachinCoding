from TicTacToe.board import Board
from TicTacToe.player import Player
from TicTacToe.playerType import PlayerType


class TicTacToe:

    def __init__(self):
        self.board = Board(3, 3)
        self.players = []
        self.players.append(Player(PlayerType.X))
        self.players.append(Player(PlayerType.Y))

    def play(self):
        player=self.players.pop(0)
        row,col=input("Enter Row and Col")
        self.board.addPlayer(row,col,player)
        if self.checkWinner(row,col)==True:
            print("Player: "+player.playerType +" won the match")
        if self.board.emptyCells==0:
            print("Game Tied")

        self.players.append(player)




    def checkWinner(self,row,col):
        #rowCheck
        #colCheck
        #diagonalCheck
        #anti-diagonalCheck

        for i in range(0,row):
            if self.board.board[row][i]=="" or self.board.board[i][]:
                print()
            if self.board.board[i][row]=="":
                print()

        pass