from piece import *
from piece import Piece

class Pawn(Piece):
    def __init__(self, currentPosition, color, board):
        self.color = color
        if color == "b":
            super().__init__(currentPosition, "bp", board)
        else:
            super().__init__(currentPosition, "wp", board)

    def getPawn(self):
        return self.currentPosition, self.color

    def setPawn(self, newPosition):
        self.currentPosition = newPosition
        return self.currentPosition

    def isValidateMovePawnTwoField(self, start, end):
        if end[0] - start[0] == 2 and start[0] == 1:
            if self.isOccupiedPosition((start[0] + 1,start[1])) == False:
                return False
        elif start[0] - end[0] == 2 and start[0] == 6:
            if self.isOccupiedPosition((start[0] - 1,start[1])) == False:
                return False
        if start[0] == 1 and end[0] - start[0] > 2:
            return False
        if start[0] == 6 and start[0] - end[0] > 2:
            return False
        if abs(start[0] - end[0]) > 2:
            return False
        return True

    def isMoreThanOneField(self, start, end):
        if start[0] != 6 and start[0] != 1:
            if abs(start[0] - end[0]) > 1:
                return False
        return True

    def isValidateDirection(self, start, end):
        if self.color == "w" and end[0] >= start[0]:
            return False
        elif self.color == "b" and end[0] <= start[0]:
            return False
        else:
            return True
    def isPawnKilling(self, start, end):
        if abs(end[0]-start[0]) == 1 and abs(end[1] - start[1]) == 1:
            if self.color == "b" and end[0]-start[0] == 1 and self.isOccupiedPosition(end) == False and self.getColorFromBoard(end) == "w":
                return "kill"
            elif self.color == "w" and start[0] - end[0] == 1 and self.isOccupiedPosition(start) == False and self.getColorFromBoard(end) == "b":
                return "kill"
            else:
                return False

    def isValidateMove(self, start, end):
        if super().isOutOfBoard(end) == True:
            return False
        if abs(end[0]-start[0]) == 1 and abs(end[1] - start[1]) == 1:
            if self.isPawnKilling(start, end) == "kill":
                return "kill"
        if start[1] != end[1]:
            return False
        elif self.isValidateDirection(start, end) == False:
            return False
        elif self.isValidateMovePawnTwoField(start, end) == False:
            return False
        elif self.isMoreThanOneField(start, end)==False:
            return False
        elif self.isOccupiedPosition(end) == False:
            return False
        return True

    def checkKills(self, currentPosition):
        if self.checkKillsOneFieldDiagonal(currentPosition) == True:
            return True
        else:
            return False