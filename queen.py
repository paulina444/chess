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

    def setQueen(self, newPosition):
        self.currentPosition = newPosition

        return self.currentPosition, self.color

    def isValidateMove(self, start, end):
        if super().isEmptyVerticalAndChorizontal(start, end) == False:
            return False
        elif super().isEmptyDiagonal(start, end) == False:
            return False
        isvalidate = super().isValidateMove(start, end)
        if isvalidate == False:
            return False
        elif isvalidate == "kill":
            return "kill"
        return True

    def checkKills(self, currentPosition):
        if self.checkKillsChorizontalandVertical(currentPosition) == True:
            return True
        elif self.checkKillsDiagonal(currentPosition) == True:
            return True
        else:
            return False

