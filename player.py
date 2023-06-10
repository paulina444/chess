#ona powinna przechowywac jakie figury piosiada gracz
# kolor moze byc wiadomy w zaleznosci od playera
from piece import *
from piece import Piece


class Player:
    def __init__(self, kolor):
        self.figury = []
        self.kolor = kolor

    def addFigury(self, figura:Piece):
        #print("XXXXXXXXXXXXx")
        #print(len(self.figury))
        self.figury.append(figura)
        #print(self.figury[-1].getPiece())

    def printFigury(self, numer):
        print(self.figury[numer].getPiece())



        #piece.move(figura.currentposition)
        #self.figury.update({obiekt: miejsce})
        #return self.figury.update({obiekt: miejsce})

    """def updateFigury(self, skad, new_position):
        #element = tutaj sie dowiemy w jakim graczu jest figura i w funkcji move
        #trzeba bedzie zaaktualizowac liste figur gracza
        #albo znalezc sposob na zamiane liczby [] na prawidlowy pionek

        index = self.figury.index(element)
        print(index)
        self.figury[14].move(skad, new_position)"""

    def getPlayer(self):
        return self.figury, self.kolor

    def getFigury(self):
        return self.figury

    def setPlayer(self, kolor):
        self.kolor = kolor
        return self.kolor
