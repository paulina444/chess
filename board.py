from cell import *
from knight import Knight
from player import *
from bishop import *
from pawn import *
from king import *
from player import Player
from queen import *
from knight import *
from rook import *
class Board:
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
        self.b1 = Bishop((0, 2), "b", szachownica)
        self.b2 = Bishop((0, 5), "b", szachownica)
        self.b3 = Bishop((7, 2), "w", szachownica)
        self.b4 = Bishop((7, 5), "w", szachownica)
        #wrzucenie biszopow do planszy
        self.place_piece(self.b1, self.b1.currentPosition)
        self.place_piece(self.b2, self.b2.currentPosition)
        self.place_piece(self.b3, self.b3.currentPosition)
        self.place_piece(self.b4, self.b4.currentPosition)
        #wrzucenie dla gracza biszopow
        self.bialyPlayer.addFigury(self.b3)
        self.bialyPlayer.addFigury(self.b4)
        self.czarnyPlayer.addFigury(self.b1)
        self.czarnyPlayer.addFigury(self.b2)

        #tworzenie pawnsow czarnych
        self.p1 = Pawn((1, 0), "b", szachownica)
        self.p2 = Pawn((1, 1), "b", szachownica)
        self.p3 = Pawn((1, 2), "b", szachownica)
        self.p4 = Pawn((1, 3), "b", szachownica)
        self.p5 = Pawn((1, 4), "b", szachownica)
        self.p6 = Pawn((1, 5), "b", szachownica)
        self.p7 = Pawn((1, 6), "b", szachownica)
        self.p8 = Pawn((1, 7), "b", szachownica)
        #wrzucenie do planszy pawnosow czarnych
        self.place_piece(self.p1, self.p1.currentPosition)
        self.place_piece(self.p2, self.p2.currentPosition)
        self.place_piece(self.p3, self.p3.currentPosition)
        self.place_piece(self.p4, self.p4.currentPosition)
        self.place_piece(self.p5, self.p5.currentPosition)
        self.place_piece(self.p6, self.p6.currentPosition)
        self.place_piece(self.p7, self.p7.currentPosition)
        self.place_piece(self.p8, self.p8.currentPosition)
        #wrzucanie dla gracza czarnych pawnsow
        self.czarnyPlayer.addFigury(self.p1)
        self.czarnyPlayer.addFigury(self.p2)
        self.czarnyPlayer.addFigury(self.p3)
        self.czarnyPlayer.addFigury(self.p4)
        self.czarnyPlayer.addFigury(self.p5)
        self.czarnyPlayer.addFigury(self.p6)
        self.czarnyPlayer.addFigury(self.p7)
        self.czarnyPlayer.addFigury(self.p8)

        # tworzenie pawnsow bialych
        self.p9 = Pawn((6, 0), "w", szachownica)
        self.p10 = Pawn((6, 1), "w", szachownica)
        self.p11 = Pawn((6, 2), "w", szachownica)
        self.p12 = Pawn((6, 3), "w", szachownica)
        self.p13 = Pawn((6, 4), "w", szachownica)
        self.p14 = Pawn((6, 5), "w", szachownica)
        self.p15 = Pawn((6, 6), "w", szachownica)
        self.p16 = Pawn((6, 7), "w", szachownica)
        # wrzucenie do planszy pawnosow bialych
        self.place_piece(self.p9, self.p9.currentPosition)
        self.place_piece(self.p10, self.p10.currentPosition)
        self.place_piece(self.p11, self.p11.currentPosition)
        self.place_piece(self.p12, self.p12.currentPosition)
        self.place_piece(self.p13, self.p13.currentPosition)
        self.place_piece(self.p14, self.p14.currentPosition)
        self.place_piece(self.p15, self.p15.currentPosition)
        self.place_piece(self.p16, self.p16.currentPosition)
        #wrzucanie dla gracza bialych pawnsow
        self.bialyPlayer.addFigury(self.p9)
        self.bialyPlayer.addFigury(self.p10)
        self.bialyPlayer.addFigury(self.p11)
        self.bialyPlayer.addFigury(self.p12)
        self.bialyPlayer.addFigury(self.p13)
        self.bialyPlayer.addFigury(self.p14)
        self.bialyPlayer.addFigury(self.p15)
        self.bialyPlayer.addFigury(self.p16)

        # tworzenie kinga
        self.k1 = King((0, 4), "b", szachownica)
        self.k2 = King((7, 4), "w", szachownica)
        # wstawienie do planszy kingow
        self.place_piece(self.k1, self.k1.currentPosition)
        self.place_piece(self.k2, self.k2.currentPosition)
        #wrzucanie do graczy kingow
        self.bialyPlayer.addFigury(self.k2)
        self.czarnyPlayer.addFigury(self.k1)

        # tworzenie queen
        self.q1 = Queen((0, 3), "b", szachownica)
        self.q2 = Queen((7, 3), "w", szachownica)
        # wstawienie do planszy queeny
        self.place_piece(self.q1, self.q1.currentPosition)
        self.place_piece(self.q2, self.q2.currentPosition)
        #wstawienie do graczt queeny
        self.bialyPlayer.addFigury(self.q2)
        self.czarnyPlayer.addFigury(self.q1)

        # tworzenie knightow
        self.n1 = Knight((0, 1), "b", szachownica)
        self.n2 = Knight((0, 6), "b", szachownica)
        self.n3 = Knight((7, 1), "w", szachownica)
        self.n4 = Knight((7, 6), "w", szachownica)
        # wstawienie do planszy knightow
        self.place_piece(self.n1, self.n1.currentPosition)
        self.place_piece(self.n2, self.n2.currentPosition)
        self.place_piece(self.n3, self.n3.currentPosition)
        self.place_piece(self.n4, self.n4.currentPosition)
        #wstawienie do graczy knightow
        self.czarnyPlayer.addFigury(self.n1)
        self.czarnyPlayer.addFigury(self.n2)
        self.bialyPlayer.addFigury(self.n3)
        self.bialyPlayer.addFigury(self.n4)

        # stworzenie rooki
        self.r1 = Rook((0, 0), "b", szachownica)
        self.r2 = Rook((0, 7), "b", szachownica)
        self.r3 = Rook((7, 0), "w", szachownica)
        self.r4 = Rook((7, 7), "w", szachownica)
        # wstawienie do planszy rooki
        self.place_piece(self.r1, self.r1.currentPosition)
        self.place_piece(self.r2, self.r2.currentPosition)
        self.place_piece(self.r3, self.r3.currentPosition)
        self.place_piece(self.r4, self.r4.currentPosition)
        #wstawienie do graczy rookow
        self.czarnyPlayer.addFigury(self.r1)
        self.czarnyPlayer.addFigury(self.r2)
        self.bialyPlayer.addFigury(self.r3)
        self.bialyPlayer.addFigury(self.r4)

    def getBialeFigury(self):
        return self.bialyPlayer.getPlayer()

    def getCzarneFigury(self):
        return self.czarnyPlayer.getPlayer()

    def removeFromListWhitePieces(self, position):
        x = self.getPieceFromBoard(position)
        self.bialyPlayer.figury.remove(x)
        return self.getBialyPlayer().figury

    def removeFromListBlackPieces(self, position):
        a = self.getPieceFromBoard(position)
        self.czarnyPlayer.figury.remove(a)
        #return self.czarnyPlayer.figury

    def removing(self, piece):
        self.czarnyPlayer.figury.remove(piece)

    def removeFromWhiteList(self, piece):
        self.bialyPlayer.figury.remove(piece)

    def addToBlackPieces(self, position):
        a = self.getPieceFromBoard(position)
        self.czarnyPlayer.figury.append(a)

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
        secondChar = self.fromLetterToNumbers(destination[0])
        firstChar = abs(int(destination[1])-8)
        return firstChar, secondChar



        #zrob taka samo funkcje w druga strone ze np z (0,0) na a8


    def randomWhitePieceFromBoard(self):
        whitePieces = self.bialyPlayer.figury
        wylosowanaFiguraBiala = random.choice(whitePieces)
        return wylosowanaFiguraBiala

    def randomBlackPieceFromBoard(self):
        blackPieces = self.czarnyPlayer.figury
        wylosowanaFiguraCzarna = random.choice(blackPieces)
        return wylosowanaFiguraCzarna



