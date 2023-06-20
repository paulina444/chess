from piece import Piece

class Knight(Piece):
    def __init__(self, currentPosition, color, board):
        self.color = color
        if color == "b":
            super().__init__(currentPosition, "bn", board)
        else:
            super().__init__(currentPosition, "wn", board)

    def getKnight(self):
        return self.currentPosition, self.color

    def setKnight(self, newPosition, newColor):
        self.currentPosition = newPosition
        self.color = newColor
        return self.currentPosition, self.color

    def validateMoveKnight(self, start, end):
        x1, y1 = start
        x, y = end
        if (x == x1+2 or x == x1-2) and (y == y1+1 or y == y1-1):
            return True
        elif (y == y1+2 or y == y1-2) and (x == x1+1 or x == x1-1):
            return True
        else:
            return False

    def isValidateMove(self, start, end):
        if self.validateMoveKnight(start, end) == False:
            return False
        isvalidate = super().isValidateMove(start, end)
        if isvalidate == False:
            return False
        elif isvalidate == "kill":
            return "kill"
        return True

    def checkKills(self, currentPosition):
        if self.checkKillsKnight(currentPosition) == True:
            return True
        else:
            return False
