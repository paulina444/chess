from game import *
"""class Main(Game):
    def play(self):
        self.nextmove = None
        while True:
            if self.nextmove == None:
                colorAi = "w"
                self.whatColorAi(colorAi)
            else:
                colorAi = "b"
                self.whatColorAi(colorAi)

            self.moveAi()
            #self.move()
            self.display_board()"""

game1 = Game()
game1.creatingNewBoard()

game1.play()










    






#koniec gry kieidy:
# krol jest szachowany i nie moze sie ruszyc
# kiedy nie ma wystarczajaco materialuu zeby ktos mogl wygrac PAT
    #np gdy jest jeden skoczek albo 2 krole
#kiedy nikt nie moze sie ruszyc to jest PAT

#trzeba zrobic roszade - w klasie king mozna podobno
#szach mata
#jakas dziwna zasada nagrana cos tam chyba w locie???? czy cos nie wolno idk serio



"""game1 = Game("b")
game1.creatingNewBoard()"""
"""game1.move((6,7), (4,7))
game1.move((4,7), (3,7))
game1.move((6,5), (4,5))
game1.move((6,6), (5,6))
game1.move((6,4), (5,4))
game1.move((6,3), (4,3))
game1.move((6,2), (4,2))"""


"""game1.display_board()
game1.moveAi()
game1.display_board()"""


"""print(game1.getBialyPlayer())
print("biale figury:")
print(game1.getBialeFigury())
print("czarne figury:")
print(game1.getCzarneFigury())

"""

#print(game1.getCellFromBoard((0,0)).piece.getPiece())














"""print("XXXXXXXXXXXXx")
game1.getCellFromBoard((2,4)).piece.checkKillsChorizontal((2,4))
print("XXXXXXXXXXXXXXx")"""



"""
print(game1.getCellFromBoard((0,0)).getPiece().type) ##TO DAJE KOLOR
print(game1.getCellFromBoard((0,0)).getPositon())
print(game1.getCellFromBoard((0,0)).getEverything())
print(game1.getCellFromBoard((0,0)).getPiece())

"""
"""#print(game1.getColorFromBoard((0,0)))

print("AAAAAAAAAAAAAaaaa")
print(game1.randomWhitePieceFromBoard())
print("AAAAAAAAAAAAAAAAAAAAAA")
"""



#print(game1.moveAi())
#############3game1.moveAi((0,0),(0,0))
#game1.getCellFromBoard((1,0)).piece.move((1,0), (2,0))
#print(type(game1.getCellFromBoard((0,0)).piece))
"""print(game1.getCellFromBoard((0,7)).getCell())
print(game1.getPieceFromBoard((0,0)))
print(game1.getCellFromBoard((1,0)).getCell())
print(game1.getCellFromBoard((1,0)).getCell())"""
"""print(game1.getCellFromBoard((3,0)).getCell())
print(game1.getCellFromBoard((0,0)).getCell())
print(game1.getCellFromBoard((4,4)).getCell())
print(game1.getCellFromBoard((0,4)).getCell())"""






