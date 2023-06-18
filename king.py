from piece import *
from piece import Piece


class King(Piece):
    def __init__(self, currentPosition, color, board):
        self.color = color
        if color == "b":
            super().__init__(currentPosition, "bk", board)
        else:
            super().__init__(currentPosition, "wk", board)

    def getKing(self):
        return self.currentPosition, self.color

    def setKing(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color


    def isValidateMove(self, start, end):
        x, y = end
        # Sprawdzenie, czy ruch jest zgodny z zasadami ruchu króla
        if abs(x - start[0]) > 1 or abs(y - start[1]) > 1:
            return False
        isvalidate = super().isValidateMove(start, end)
        if isvalidate == False:
            return False
        elif isvalidate == "kill":
            return "kill"
        return True

    def checkKills(self, currentPosition):
        if self.checkKillsOneField(currentPosition) == True:
            return True
        else:
            return False

