from piece import Piece

class Player:
    def __init__(self, kolor):
        self.figury = []
        self.kolor = kolor

    def getPlayer(self):
        return self.figury, self.kolor

    def getFigury(self):
        return self.figury

    def setPlayer(self, kolor):
        self.kolor = kolor
        return self.kolor

    def addFigury(self, figura:Piece):
        self.figury.append(figura)


