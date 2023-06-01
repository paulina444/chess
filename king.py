from piece import *
from piece import Piece


class King(Piece):
    def __init__(self, currentPosition, color, board):
        self.color = color
        if color == "b":
            super().__init__(currentPosition, "bk", board)
        else:
            super().__init__(currentPosition, "wk", board)

    def getColor(self):
        return self.color

    def getKing(self):
        return self.currentPosition, self.color

    def setKing(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color

    def update(self, newPosition):
        self.currentPosition = newPosition
        return self.currentPosition, self.color

    def isValidateMove(self, destination, skad):
        x, y = self.new_position
        if super().isValidateMove(destination, skad) == False:
            return False
        # Sprawdzenie, czy ruch jest zgodny z zasadami ruchu króla
        if abs(x - self.currentPosition[0]) > 1 or abs(y - self.currentPosition[1]) > 1:
            print("Nieprawidłowy ruch - król może poruszać się o co najwyżej jedno pole w dowolnym kierunku.")
            return False
        else:
            print("PRAWIDLOWY RUCH")
            return True

    def move(self, skad, new_position):
        super().move(skad, new_position)
        self.skad = self.currentPosition  # np k1.currentPosition luub self.skad = skad
        self.new_position = new_position
        if self.isValidateMove(new_position, skad) == True:
            self.move_base(new_position)
