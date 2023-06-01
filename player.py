#ona powinna przechowywac jakie figury piosiada gracz
# kolor moze byc wiadomy w zaleznosci od playera
from piece import *
class Player:
    def __init__(self, kolor):
        self.figury = {}
        self.kolor = kolor

    def updateFigury(self, figura:Piece, miejsce):
        """figura.currentPosition
        self.figury.get(figura)
        piece.move(figura.currentposition)"""
        self.figury.update({obiekt: miejsce})
        return self.figury.update({obiekt: miejsce})

    def getPlayer(self):
        return self.figury, self.kolor

    def setPlayer(self, kolor):
        self.kolor = kolor
        return self.kolor
