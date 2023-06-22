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
        self.chessboard = [[Cell(x, y) for x in range(8)] for y in range(8)]

    def getBoard(self):
        return self.chessboard

    def getCellFromBoard(self, position):
        x, y = position
        return self.chessboard[x][y]

    def getColorFromBoard(self, position):
        x, y = position
        return self.getCellFromBoard((x,y)).getPiece().color

    def getPieceFromBoard(self, position):
        x, y = position
        cell = self.chessboard[x][y]
        piece = cell.getPiece()
        return piece

    def placePiece(self, piece, position):
        x, y = position
        self.chessboard[x][y].setCell(x, y, piece)

    def displayBoard(self):
        print("   A  B  C  D  E  F  G  H ")
        for i, row in enumerate(self.chessboard):
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
        chessboard = self.chessboard
        self.whitePlayer = Player("white")
        self.blackPlayer = Player("black")

        #stworzenie biszopow
        self.b1 = Bishop((0, 2), "b", chessboard)
        self.b2 = Bishop((0, 5), "b", chessboard)
        self.b3 = Bishop((7, 2), "w", chessboard)
        self.b4 = Bishop((7, 5), "w", chessboard)

        #wrzucenie biszopow do planszy
        self.placePiece(self.b1, self.b1.currentPosition)
        self.placePiece(self.b2, self.b2.currentPosition)
        self.placePiece(self.b3, self.b3.currentPosition)
        self.placePiece(self.b4, self.b4.currentPosition)

        #wrzucenie dla gracza biszopow
        self.whitePlayer.addFigury(self.b3)
        self.whitePlayer.addFigury(self.b4)
        self.blackPlayer.addFigury(self.b1)
        self.blackPlayer.addFigury(self.b2)

        #tworzenie pawnsow czarnych
        self.p1 = Pawn((1, 0), "b", chessboard)
        self.p2 = Pawn((1, 1), "b", chessboard)
        self.p3 = Pawn((1, 2), "b", chessboard)
        self.p4 = Pawn((1, 3), "b", chessboard)
        self.p5 = Pawn((1, 4), "b", chessboard)
        self.p6 = Pawn((1, 5), "b", chessboard)
        self.p7 = Pawn((1, 6), "b", chessboard)
        self.p8 = Pawn((1, 7), "b", chessboard)

        #wrzucenie do planszy pawnosow czarnych
        self.placePiece(self.p1, self.p1.currentPosition)
        self.placePiece(self.p2, self.p2.currentPosition)
        self.placePiece(self.p3, self.p3.currentPosition)
        self.placePiece(self.p4, self.p4.currentPosition)
        self.placePiece(self.p5, self.p5.currentPosition)
        self.placePiece(self.p6, self.p6.currentPosition)
        self.placePiece(self.p7, self.p7.currentPosition)
        self.placePiece(self.p8, self.p8.currentPosition)

        #wrzucanie dla gracza czarnych pawnsow
        self.blackPlayer.addFigury(self.p1)
        self.blackPlayer.addFigury(self.p2)
        self.blackPlayer.addFigury(self.p3)
        self.blackPlayer.addFigury(self.p4)
        self.blackPlayer.addFigury(self.p5)
        self.blackPlayer.addFigury(self.p6)
        self.blackPlayer.addFigury(self.p7)
        self.blackPlayer.addFigury(self.p8)

        # tworzenie pawnsow bialych
        self.p9 = Pawn((6, 0), "w", chessboard)
        self.p10 = Pawn((6, 1), "w", chessboard)
        self.p11 = Pawn((6, 2), "w", chessboard)
        self.p12 = Pawn((6, 3), "w", chessboard)
        self.p13 = Pawn((6, 4), "w", chessboard)
        self.p14 = Pawn((6, 5), "w", chessboard)
        self.p15 = Pawn((6, 6), "w", chessboard)
        self.p16 = Pawn((6, 7), "w", chessboard)

        # wrzucenie do planszy pawnosow bialych
        self.placePiece(self.p9, self.p9.currentPosition)
        self.placePiece(self.p10, self.p10.currentPosition)
        self.placePiece(self.p11, self.p11.currentPosition)
        self.placePiece(self.p12, self.p12.currentPosition)
        self.placePiece(self.p13, self.p13.currentPosition)
        self.placePiece(self.p14, self.p14.currentPosition)
        self.placePiece(self.p15, self.p15.currentPosition)
        self.placePiece(self.p16, self.p16.currentPosition)

        #wrzucanie dla gracza bialych pawnsow
        self.whitePlayer.addFigury(self.p9)
        self.whitePlayer.addFigury(self.p10)
        self.whitePlayer.addFigury(self.p11)
        self.whitePlayer.addFigury(self.p12)
        self.whitePlayer.addFigury(self.p13)
        self.whitePlayer.addFigury(self.p14)
        self.whitePlayer.addFigury(self.p15)
        self.whitePlayer.addFigury(self.p16)

        # tworzenie kinga
        self.k1 = King((0, 4), "b", chessboard)
        self.k2 = King((7, 4), "w", chessboard)

        # wstawienie do planszy kingow
        self.placePiece(self.k1, self.k1.currentPosition)
        self.placePiece(self.k2, self.k2.currentPosition)

        #wrzucanie do graczy kingow
        self.whitePlayer.addFigury(self.k2)
        self.blackPlayer.addFigury(self.k1)

        # tworzenie queen
        self.q1 = Queen((0, 3), "b", chessboard)
        self.q2 = Queen((7, 3), "w", chessboard)

        # wstawienie do planszy queeny
        self.placePiece(self.q1, self.q1.currentPosition)
        self.placePiece(self.q2, self.q2.currentPosition)

        #wstawienie do graczt queeny
        self.whitePlayer.addFigury(self.q2)
        self.blackPlayer.addFigury(self.q1)

        # tworzenie knightow
        self.n1 = Knight((0, 1), "b", chessboard)
        self.n2 = Knight((0, 6), "b", chessboard)
        self.n3 = Knight((7, 1), "w", chessboard)
        self.n4 = Knight((7, 6), "w", chessboard)

        # wstawienie do planszy knightow
        self.placePiece(self.n1, self.n1.currentPosition)
        self.placePiece(self.n2, self.n2.currentPosition)
        self.placePiece(self.n3, self.n3.currentPosition)
        self.placePiece(self.n4, self.n4.currentPosition)

        #wstawienie do graczy knightow
        self.blackPlayer.addFigury(self.n1)
        self.blackPlayer.addFigury(self.n2)
        self.whitePlayer.addFigury(self.n3)
        self.whitePlayer.addFigury(self.n4)

        # stworzenie rooki
        self.r1 = Rook((0, 0), "b", chessboard)
        self.r2 = Rook((0, 7), "b", chessboard)
        self.r3 = Rook((7, 0), "w", chessboard)
        self.r4 = Rook((7, 7), "w", chessboard)

        # wstawienie do planszy rooki
        self.placePiece(self.r1, self.r1.currentPosition)
        self.placePiece(self.r2, self.r2.currentPosition)
        self.placePiece(self.r3, self.r3.currentPosition)
        self.placePiece(self.r4, self.r4.currentPosition)

        #wstawienie do graczy rookow
        self.blackPlayer.addFigury(self.r1)
        self.blackPlayer.addFigury(self.r2)
        self.whitePlayer.addFigury(self.r3)
        self.whitePlayer.addFigury(self.r4)

    def removeFromListWhitePieces(self, position):
        x = self.getPieceFromBoard(position)
        self.whitePlayer.figury.remove(x)
        return self.whitePlayer.figury

    def removeFromListBlackPieces(self, position):
        a = self.getPieceFromBoard(position)
        self.blackPlayer.figury.remove(a)
        return self.blackPlayer.figury

    def removing(self, piece):
        self.blackPlayer.figury.remove(piece)

    def removeFromWhiteList(self, piece):
        self.whitePlayer.figury.remove(piece)

    def addToBlackPieces(self, position):
        piece = self.getPieceFromBoard(position)
        self.blackPlayer.figury.append(piece)

    def fromLetterToNumbers(self, argument):
        letter_to_number = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7
        }
        for letter, number in letter_to_number.items():
            if letter == argument:
                return number

    def convertToBoard(self, destination):
        secondChar = self.fromLetterToNumbers(destination[0])
        firstChar = abs(int(destination[1])-8)
        return firstChar, secondChar

    def randomWhitePieceFromBoard(self):
        whitePieces = self.whitePlayer.figury
        randomPieceWhite = random.choice(whitePieces)
        return randomPieceWhite

    def randomBlackPieceFromBoard(self):
        blackPieces = self.blackPlayer.figury
        randomPieceBlack = random.choice(blackPieces)
        return randomPieceBlack



