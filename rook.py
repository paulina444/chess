from piece import *
from piece import Piece
from player import *

class Rook(Piece):
    def __init__(self, currentPosition, color, board):
        self.color = color
        if color == "b":
            super().__init__(currentPosition, "br", board)
        else:
            super().__init__(currentPosition, "wr", board)

    def getRook(self):
        return self.currentPosition, self.color

    def setRook(self, newPosition):
        self.currentPosition = newPosition
        return self.currentPosition

    def isValidateMove(self, start, end):
        x, y = end
        if x != start[0] and y != start[1]:
            return False
        elif super().isEmptyVerticalAndChorizontal(start, end) == False:
            return False
        validateMove = super().isValidateMove(start, end)
        if validateMove == False:
            return False
        elif validateMove == "kill":
            return "kill"

        return True

    def checkKills(self, currentPosition):
        if self.checkKillsChorizontalandVertical(currentPosition) == True:
            return True
        else:
            return False







