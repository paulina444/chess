from piece import *
from piece import Piece
class Queen(Piece):
    def __init__(self, currentPosition, color, board):
        self.color = color
        if color == "b":
            super().__init__(currentPosition, "bq", board)
        else:
            super().__init__(currentPosition, "wq", board)

    def getQueen(self):
        return self.currentPosition, self.color

    def setQueen(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color

    def isValidateMove(self,destination, skad):
        if super().isEmptyVertical(self.currentPosition, self.new_position) == False: #przeskakuje pionki
            return False
        elif super().isEmptyHorizontal(self.currentPosition, self.new_position) == False:
            return False
        elif super().isEmptySkosy(self.currentPosition, self.new_position) == False:
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
            self.move_base(self.new_position)
            return True
        else:
            return False

