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

    def setRook(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color

    def isValidateMove(self, start, end):
        x, y = end
        # Sprawdzenie, czy ruch jest zgodny z zasadami ruchu wieży
        if x != start[0] and y != start[1]:
            return False
        elif super().isEmptyVertical(start, end) == False: #przeskakuje pionki
            return False
        elif super().isEmptyHorizontal(start, end) == False:
            return False

        validateMove = super().isValidateMove(start, end)
        if validateMove == False:
            return False
        elif validateMove == "kill":
            return "kill"

        return True

    def checkKills(self, currentPosition):
        if self.checkKillsChorizontal(currentPosition) == True:
            return True
        elif self.checkKillsVertical(currentPosition) == True:
            return True
        else:
            return False







