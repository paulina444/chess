from game import *
game1 = Game()
game1.creatingNewBoard()
"""game1.display_board()
game1.move((1,2),(3,2))
game1.display_board()

game1.move((6,3),(4,3))
game1.display_board()
game1.move((3,2),(4,3))
game1.display_board()
game1.move((4,3),(6,3))
print("vdfdf")
game1.display_board()

game1.move((1,0),(2,0))
game1.display_board()
game1.move((2,0),(4,0))
game1.move((2,0),(2,1))
game1.move((4,3),(7,3))
game1.move((4,3),(5,3))

print("4")
game1.display_board()

game1.getPieceFromBoard((7,6)).remove_piece((7,6))
game1.getPieceFromBoard((7,5)).remove_piece((7,5))
game1.getPieceFromBoard((7,7)).remove_piece((7,7))
game1.display_board()
print("2")

game1.move((7,4),(7,5))
game1.move((7,5),(7,6))
game1.move((6,4),(4,4))
game1.move((2,0),(3,0))
game1.move((0,0),(2,0))

game1.move((2,0),(2,4))
game1.move((1,3),(2,3))
game1.move((4,4),(3,4))

game1.move((3,4),(2,3))

game1.display_board()
game1.move((2,4),(7,4))
game1.display_board()
print("1")

game1.move((7,4),(7,3))
game1.display_board()
"""




game1.display_board()
game1.move((6,1),(4,1))
game1.move((4,1),(3,1))
game1.move((3,1),(2,1))
print(game1.getCellFromBoard((0,0)).piece.isValidateMove((0,0),(2,0)))
print(game1.getCellFromBoard((1,0)).piece)
print(game1.getCellFromBoard((1,0)).piece.isValidateMove((1,0),(2,1)))
print(game1.getCellFromBoard((0,7)).piece.isValidateMove((0,7),(3,4)))
game1.getCellFromBoard((0,7)).piece.move_base((4,3))
print(game1.getCellFromBoard((4,3)).piece.isValidateMove((4,3),(3,4)))
game1.getCellFromBoard((7,0)).piece.move_base((5,2))
print(game1.getCellFromBoard((4,3)).piece.isValidateMove((4,3),(5,2)))

game1.display_board()
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






