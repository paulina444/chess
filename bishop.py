from piece import *
from piece import Piece


class Bishop(Piece):
    def __init__(self, currentPosition, color, board):
        self.color = color
        if color == "b":
            super().__init__(currentPosition, "bb", board)
        else:
            super().__init__(currentPosition, "wb", board)

    def getColor(self):
        return self.color

    def getBishop(self):
        return self.currentPosition, self.color

    def setBishop(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color

    def update(self, newPosition):
        self.currentPosition = newPosition
        return self.currentPosition, self.color

    def isValidateMove(self, destination, skad):
        if super().isEmptySkosy(self.skad, self.new_position) == False:
            print("nieprawidlowy ruch - przeskakujesz pionki lub ruch nie jest na skos")
            return False
        elif super().isValidateMove(destination, skad) == False:
            return False
        else:
            return True

    def move(self, skad, new_position):
        super().move(skad, new_position)
        self.skad = self.currentPosition
        self.new_position = new_position
        if self.isValidateMove(new_position, skad) == True:
            print("jej tu powinno zrobic ruch")
            self.move_base(self.new_position)


    def __del__(self): #gdy bedzie bicie to bedzie trzeba zrobic del mojbishop
        pass