from piece import *
from piece import Piece

# 2. gdy pionki dojda do konca planszy moga sie zamienic w inna figure
    # nie wazne czy z zabitych czy nie z zabitych


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

    def isValidateMove(self, destination, skad):
        x, y = self.new_position
        if super().is_valid_position(destination) == False:
            return False
        #bicia
        elif abs(x-self.currentPosition[0]) == 1 and abs(y - self.currentPosition[1]) == 1:
            if super().getColorFromBoard(self.currentPosition) == 'b' and x-self.currentPosition[0] == 1 and super().is_occupied_position(destination)==False and super().getColorFromBoard(self.new_position) == 'w' :
                super().remove_piece((x,y))
                return True
            elif super().getColorFromBoard(self.currentPosition) == 'w' and self.currentPosition[0] - x == 1 and  super().is_occupied_position(destination)==False and super().getColorFromBoard(self.new_position) == 'b':
                super().remove_piece((x, y))
                return True
            else:
                return False
            # Sprawdzenie, czy ruch jest zgodny z kierunkiem poruszania się pionka
        elif self.color == "w" and x >= self.currentPosition[0]:
            return False
        elif self.color == "b" and x <= self.currentPosition[0]:
            return False
        elif (self.currentPosition[0] == 1 or self.currentPosition[0] == 6) and (abs(x - self.currentPosition[0]) > 2 or abs(y - self.currentPosition[1] != 0)):
            return False
        elif self.currentPosition[0] != 1 and self.currentPosition[0] != 6 and (abs(x - self.currentPosition[0] > 1) or abs(y - self.currentPosition[1] != 0)):
            return False
        elif super().is_occupied_position(destination) == False:
            return False
        else:
            return True
        """elif self.color == "w" and self.currentPosition[0] == 0:
                    self.remove_piece(skad)
                elif self.color == "b" and self.currentPosition[0] == 7:
                    self.remove_piece(skad)"""

    def move(self, skad, new_position):
        super().move(skad, new_position)
        self.skad = self.currentPosition
        self.new_position = new_position
        if self.isValidateMove(new_position, skad) == True:
            self.move_base(self.new_position)
            return True
        else:
            return False

    def __del__(self): #gdy bedzie bicie to bedzie trzeba zrobic del mojbishop
        pass