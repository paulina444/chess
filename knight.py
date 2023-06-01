from piece import *
from piece import Piece


class Knight(Piece):
    def __init__(self, currentPosition, color, board):
        self.color = color
        if color == "b":
            super().__init__(currentPosition, "bn", board)
        else:
            super().__init__(currentPosition, "wn", board)

    def getColor(self):
        return self.color

    def getKnight(self):
        return self.currentPosition, self.color

    def setKnight(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color

    def update(self, newPosition):
        self.currentPosition = newPosition
        return self.currentPosition, self.color

    def validateMoveKnight(self):
        x1, y1 = self.currentPosition
        x, y = self.new_position
        if (x == x1+2 or x == x1-2) and (y == y1+1 or y == y1-1):
            return True
        elif (y == y1+2 or y == y1-2) and (x == x1+1 or x == x1-1):
            return True
        else:
            return False


    def isValidateMove(self, destination, skad):
        x1, y1 = self.currentPosition
        x, y = self.new_position
        if super().isValidateMove(destination, skad) == False:
            return False
        elif self.validateMoveKnight() == False:
            print("zły ruch konia")
        else:
            return True

    def move(self, skad, new_position):
        super().move(skad, new_position)
        self.skad = self.currentPosition
        self.new_position = new_position
        if self.isValidateMove(new_position, skad) == True:
            self.move_base(self.new_position)



    def __del__(self): #gdy bedzie bicie to bedzie trzeba zrobic del mojbishop
        pass