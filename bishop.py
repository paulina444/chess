from piece import *
from piece import Piece
class Bishop(Piece):
    def __init__(self, currentPosition, color, board):
        self.color = color
        if color == "b":
            super().__init__(currentPosition, "bb", board)
        else:
            super().__init__(currentPosition, "wb", board)

    def getBishop(self):
        return self.currentPosition, self.color

    def setBishop(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color


    def isValidateMove(self, start, end):
        if start[0]==end[0] or start[1]==end[1]:
            return False
        if super().isEmptySkosy(start, end) == False:
            return False
        isvalidate = super().isValidateMove(start, end)
        if isvalidate == False:
            return False
        elif isvalidate == "kill":
            return "kill"

        return True

    def checkKills(self, currentPosition):
        if self.checkKillsSkosy(currentPosition) == True:
            return True
        else:
            return False




