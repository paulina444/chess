from board import *
from cell import *
class Game(Board):
    def __init__(self):
        super().__init__()

    def getGame(self):
        return self.whitePlayer, self.blackPlayer, self.board

    def setGame(self, newWhitePlayer, newBlackPlayer, newBoard):
        self.whitePlayer = newWhitePlayer
        self.blackPlayer = newBlackPlayer
        self.board = newBoard
        return self.whitePlayer, self.blackPlayer, self.board


    def move(self, skad, dokad):
        if self.getPieceFromBoard(skad) is None:
            print("nie ma pionka na pozycji startujacej")
            return False
        return self.getCellFromBoard(skad).piece.move(skad, dokad)

    def nextMove(self, opponentMove = None):
        pass

    def isGameOver(self):
        pass


