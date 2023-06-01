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

    def getColor(self):
        return self.color

    def getRook(self):
        return self.currentPosition, self.color

    def setRook(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color

    def update(self, newPosition):
        self.currentPosition = newPosition
        return self.currentPosition, self.color

    def isValidateMove(self, destination, skad):
        x, y = self.new_position
        # Sprawdzenie, czy ruch jest zgodny z zasadami ruchu wieży
        if x != self.currentPosition[0] and y != self.currentPosition[1]:
            print("Nieprawidłowy ruch - wieża może poruszać się tylko wzdłuż jednej osi (poziomej lub pionowej).")
            return False
        elif super().isEmptyVertical(self.currentPosition, self.new_position) == False: #przeskakuje pionki
            print("Twoja wierza przeskakuje pionki")
            return False
        elif super().isEmptyHorizontal(self.currentPosition, self.new_position) == False:
            print("Twoja wierza przeskakuje pionki")
            return False
        elif super().isValidateMove(destination, skad) == False:
            return False
        else:
            print("PRAWIDLOWY RUCH")
            return True

    def move(self, skad, new_position):
        super().move(skad, new_position)
        self.skad = self.currentPosition
        self.new_position = new_position #idk czy ta linijka potrzebna
        if self.isValidateMove(new_position, skad) == True:
            self.move_base(self.new_position)




    def __del__(self): #gdy bedzie bicie to bedzie trzeba zrobic del mojbishop
        pass