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

    def setPawn(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color

    def isValidateMovePawnTwoField(self, skad, dokad):
        if dokad[0] - skad[0] == 2 and skad[0] == 1:
            if self.is_occupied_position((skad[0] + 1,skad[1])) == False:
                return False #przeskakuj pionek
        elif skad[0] - dokad[0] == 2 and skad[0] == 6:
            if self.is_occupied_position((skad[0] - 1,skad[1])) == False:
                return False #przeskakuj pionek
        if skad[0] == 1 and dokad[0] - skad[0] > 2:
            return False
        if skad[0] == 6 and skad[0] - dokad[0] > 2:
            return False
        if abs(skad[0]- dokad[0])>2:
            return False
        return True

    def isMoreThanOneField(self, start,end):
        if start[0] != 6 and start[0] != 1:
            if abs(start[0] - end[0]) > 1:
                return False
        return True

    def isValidateDirection(self, start,end):
        if self.color == "w" and end[0] >= start[0]:
            return False
        elif self.color == "b" and end[0] <= start[0]:
            return False
        else:
            return True
    def isPawnKilling(self,start, end):
        if abs(end[0]-start[0]) == 1 and abs(end[1] - start[1]) == 1:
            if self.color == "b" and end[0]-start[0] == 1 and self.is_occupied_position(end) == False and self.getColorFromBoard(end) == "w":
                return "kill"
            elif self.color == "w" and start[0] - end[0] == 1 and self.is_occupied_position(start) == False and self.getColorFromBoard(end) == "b":
                return "kill"
            else:
                return False


    def isValidateMove(self, start,end):
        x, y = end
        if super().is_valid_position(end) == False:
            return False
        #bicia
        if abs(end[0]-start[0]) == 1 and abs(end[1] - start[1]) == 1:
            if self.isPawnKilling(start, end) == "kill":
                return "kill"
        if start[1]   != end[1]:
            return False
            # Sprawdzenie, czy ruch jest zgodny z kierunkiem poruszania się pionka
        elif self.isValidateDirection(start, end) == False:
            return False
        elif self.isValidateMovePawnTwoField(start, end) == False:
            return False
        elif self.isMoreThanOneField(start, end)==False:
            return False
        elif self.is_occupied_position(end) == False:
            return False

        return True

    def checkKills(self, currentPosition):
        if self.checkKillsOneFieldSkosy(currentPosition) == True:
            return True
        else:
            return False


