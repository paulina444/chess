from cell import *
from player import *
from bishop import *
from pawn import *
from king import *
from queen import *
from knight import *
from rook import *
class Board():
    def __init__(self):
        self.szachownica = [[Cell(x, y) for x in range(8)] for y in range(8)]

    def getBoard(self):
        return self.szachownica

    def getCellFromBoard(self, position):
        x, y = position
        return self.szachownica[x][y]

    def getColorFromBoard(self, position):
        x, y = position
        return self.getCellFromBoard((x,y)).getPiece().color

    def getPieceFromBoard(self, position):
        x, y = position
        cell = self.szachownica[x][y]
        pionek = cell.getPiece()
        return pionek

    def place_piece(self, piece, position): #ustawia pionki
        x, y = position
        self.szachownica[x][y].setCell(x, y, piece)

    def remove_piece(self, position):
        x, y = position
        self.szachownica[x][y].setCell(x, y, None)


    def display_board(self):
        print("   A  B  C  D  E  F  G  H ")
        for i, row in enumerate(self.szachownica):
            print(f"{8 - i} ", end='')
            for cell in row:
                if cell.piece is not None:
                    print(cell.piece.type, end=' ')
                else:
                    print("?  ", end='')
            print(f" {8 - i}")
        print("   A  B  C  D  E  F  G  H ")
        print()


    def creatingNewBoard(self):
        szachownica = self.szachownica
        self.bialyPlayer = Player("white")
        self.czarnyPlayer = Player("black")

        #stworzenie biszopow
        b1 = Bishop((0, 2), "b", szachownica)
        b2 = Bishop((0, 5), "b", szachownica)
        b3 = Bishop((7, 2), "w", szachownica)
        b4 = Bishop((7, 5), "w", szachownica)
        #wrzucenie biszopow do planszy
        self.place_piece(b1, b1.currentPosition)
        self.place_piece(b2, b2.currentPosition)
        self.place_piece(b3, b3.currentPosition)
        self.place_piece(b4, b4.currentPosition)
        #wrzucenie dla gracza biszopow
        self.bialyPlayer.updateFigury(b3.type, b3.currentPosition)
        self.bialyPlayer.updateFigury(b4.type, b4.currentPosition)
        self.czarnyPlayer.updateFigury(b1.type, b1.currentPosition)
        self.czarnyPlayer.updateFigury(b2.type, b2.currentPosition)

        #tworzenie pawnsow czarnych
        p1 = Pawn((1, 0), "b", szachownica)
        p2 = Pawn((1, 1), "b", szachownica)
        p3 = Pawn((1, 2), "b", szachownica)
        p4 = Pawn((1, 3), "b", szachownica)
        p5 = Pawn((1, 4), "b", szachownica)
        p6 = Pawn((1, 5), "b", szachownica)
        p7 = Pawn((1, 6), "b", szachownica)
        p8 = Pawn((1, 7), "b", szachownica)
        #wrzucenie do planszy pawnosow czarnych
        self.place_piece(p1, p1.currentPosition)
        self.place_piece(p2, p2.currentPosition)
        self.place_piece(p3, p3.currentPosition)
        self.place_piece(p4, p4.currentPosition)
        self.place_piece(p5, p5.currentPosition)
        self.place_piece(p6, p6.currentPosition)
        self.place_piece(p7, p7.currentPosition)
        self.place_piece(p8, p8.currentPosition)
        #wrzucanie dla gracza czarnych pawnsow
        self.czarnyPlayer.updateFigury(p1.type, p1.currentPosition)
        self.czarnyPlayer.updateFigury(p2.type, p2.currentPosition)
        self.czarnyPlayer.updateFigury(p3.type, p3.currentPosition)
        self.czarnyPlayer.updateFigury(p4.type, p4.currentPosition)
        self.czarnyPlayer.updateFigury(p5.type, p5.currentPosition)
        self.czarnyPlayer.updateFigury(p6.type, p6.currentPosition)
        self.czarnyPlayer.updateFigury(p7.type, p7.currentPosition)
        self.czarnyPlayer.updateFigury(p8.type, p8.currentPosition)

        # tworzenie pawnsow bialych
        p9 = Pawn((6, 0), "w", szachownica)
        p10 = Pawn((6, 1), "w", szachownica)
        p11 = Pawn((6, 2), "w", szachownica)
        p12 = Pawn((6, 3), "w", szachownica)
        p13 = Pawn((6, 4), "w", szachownica)
        p14 = Pawn((6, 5), "w", szachownica)
        p15 = Pawn((6, 6), "w", szachownica)
        p16 = Pawn((6, 7), "w", szachownica)
        # wrzucenie do planszy pawnosow bialych
        self.place_piece(p9, p9.currentPosition)
        self.place_piece(p10, p10.currentPosition)
        self.place_piece(p11, p11.currentPosition)
        self.place_piece(p12, p12.currentPosition)
        self.place_piece(p13, p13.currentPosition)
        self.place_piece(p14, p14.currentPosition)
        self.place_piece(p15, p15.currentPosition)
        self.place_piece(p16, p16.currentPosition)
        #wrzucanie dla gracza bialych pawnsow
        self.bialyPlayer.updateFigury(p9.type, p9.currentPosition)
        self.bialyPlayer.updateFigury(p10.type, p10.currentPosition)
        self.bialyPlayer.updateFigury(p11.type, p11.currentPosition)
        self.bialyPlayer.updateFigury(p12.type, p12.currentPosition)
        self.bialyPlayer.updateFigury(p13.type, p13.currentPosition)
        self.bialyPlayer.updateFigury(p14.type, p14.currentPosition)
        self.bialyPlayer.updateFigury(p15.type, p15.currentPosition)
        self.bialyPlayer.updateFigury(p16.type, p16.currentPosition)

        # tworzenie kinga
        k1 = King((0, 4), "b", szachownica)
        k2 = King((7, 4), "w", szachownica)
        # wstawienie do planszy kingow
        self.place_piece(k1, k1.currentPosition)
        self.place_piece(k2, k2.currentPosition)
        #wrzucanie do graczy kingow
        self.bialyPlayer.updateFigury(k2.type, k2.currentPosition)
        self.czarnyPlayer.updateFigury(k1.type, k1.currentPosition)

        # tworzenie queen
        q1 = Queen((0, 3), "b", szachownica)
        q2 = Queen((7, 3), "w", szachownica)
        # wstawienie do planszy queeny
        self.place_piece(q1, q1.currentPosition)
        self.place_piece(q2, q2.currentPosition)
        #wstawienie do graczt queeny
        self.bialyPlayer.updateFigury(q2.type, q2.currentPosition)
        self.czarnyPlayer.updateFigury(q1.type, q1.currentPosition)

        # tworzenie knightow
        n1 = Knight((0, 1), "b", szachownica)
        n2 = Knight((0, 6), "b", szachownica)
        n3 = Knight((7, 1), "w", szachownica)
        n4 = Knight((7, 6), "w", szachownica)
        # wstawienie do planszy knightow
        self.place_piece(n1, n1.currentPosition)
        self.place_piece(n2, n2.currentPosition)
        self.place_piece(n3, n3.currentPosition)
        self.place_piece(n4, n4.currentPosition)
        #wstawienie do graczy knightow
        self.czarnyPlayer.updateFigury(n1.type, n1.currentPosition)
        self.czarnyPlayer.updateFigury(n2.type, n2.currentPosition)
        self.bialyPlayer.updateFigury(n3.type, n3.currentPosition)
        self.bialyPlayer.updateFigury(n4.type, n4.currentPosition)

        # stworzenie rooki
        r1 = Rook((0, 0), "b", szachownica)
        r2 = Rook((0, 7), "b", szachownica)
        r3 = Rook((7, 0), "w", szachownica)
        r4 = Rook((7, 7), "w", szachownica)
        # wstawienie do planszy rooki
        self.place_piece(r1, r1.currentPosition)
        self.place_piece(r2, r2.currentPosition)
        self.place_piece(r3, r3.currentPosition)
        self.place_piece(r4, r4.currentPosition)
        #wstawienie do planszy rookow
        self.czarnyPlayer.updateFigury(r1.type, r1.currentPosition)
        self.czarnyPlayer.updateFigury(r2.type, r2.currentPosition)
        self.bialyPlayer.updateFigury(r3.type, r3.currentPosition)
        self.bialyPlayer.updateFigury(r4.type, r4.currentPosition)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(self.bialyPlayer.figury)



    def getBialeFigury(self):
        return self.bialyPlayer.getPlayer()

    def getCzarneFigury(self):
        return self.czarnyPlayer.getPlayer()

    def getBialyPlayer(self):
        return self.bialyPlayer


    def fromLetterToNumbers(self, argument):
        match argument:
            case "A":
                return 0
            case "B":
                return 1
            case "C":
                return 2
            case "D":
                return 3
            case "E":
                return 4
            case "F":
                return 5
            case "G":
                return 6
            case "H":
                return 7

    def convertToBoard(self, destination):
        firstChar = self.fromLetterToNumbers(destination[0])
        print(firstChar)
        secondChar = abs(int(destination[1])-8)
        print(secondChar)
        return firstChar, secondChar

        #zrob taka samo funkcje w druga strone ze np z (0,0) na a8




