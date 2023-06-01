class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None

    def getCell(self):
        return self.x, self.y, self.piece

    def getPiece(self):
        return self.piece

    def setCell(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece
        return self.x, self.y, self.piece