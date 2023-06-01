from game import *


#koniec gry kieidy:
# krol jest szachowany i nie moze sie ruszyc
# kiedy nie ma wystarczajaco materialuu zeby ktos mogl wygrac PAT
    #np gdy jest jeden skoczek albo 2 krole
#kiedy nikt nie moze sie ruszyc to jest PAT

#trzeba zrobic roszade - w klasie king mozna podobno
#szach mata
#jakas dziwna zasada nagrana cos tam chyba w locie???? czy cos nie wolno idk serio




#jezeli nie bedzie poprzedniego ruchu to znaczy ze ejstes bialym (mozna to wywnioskowac z interfejsu co jest na gicie)


# 1 sprawdz co zrb w pawns
# 2 sprawdzic bicia pawns
# 3 spawdzic hypkiego interface

# 1. rozdzielic na czarny bialy i kogo ruch
# 2. bicia
# 3. zobaczyc tamte metody styatyczne i czy mozna przeniesc to isEmpty vertical itd do klasy board czy cos


game1 = Game()
game1.creatingNewBoard()
game1.display_board()
print(game1.getBialyPlayer())

print(game1.getBialeFigury())
print(game1.getCzarneFigury())


#print(game1.getCellFromBoard((0,0)).piece.getPiece())




game1.move((1,0), (3,0))
game1.move((3,0), (4,0))
game1.move((6,1), (5,0))
game1.move((6,7), (4,7))
game1.move((7,7), (5,7))
game1.move((4,0), (5,0))
game1.move((6,1), (5,1))
game1.move((5,1), (4,1))


print(game1.getBialeFigury())
print(game1.bialyPlayer.figury.update({'wq': (5,2)}))
print(game1.getBialeFigury())








game1.display_board()


print(game1.getCellFromBoard((0,0)).getPiece().color) ##TO DAJE KOLOR
#print(game1.getColorFromBoard((0,0)))



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






