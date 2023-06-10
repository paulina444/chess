from board import *
from cell import *
import random
class Game(Board):
    def __init__(self):
        #self.color = color
        super().__init__()


#jesli wpisze cos zlego do terminala? to sie wywala

    def play(self):
        self.nextmove = None
        while True:
            if self.nextmove == None:
                colorAi = "w"
                self.whatColorAi(colorAi)
            else:
                colorAi = "b"
                self.whatColorAi(colorAi)

            if colorAi == "w":

                self.moveAi()

                self.display_board()
                print("Graczu podaj gdzie chcesz sie ruszyc")
                skad = input(int())
                dokad = input(int())
                x = self.convertToBoard(skad)
                y = self.convertToBoard(dokad)


                if self.move(x,y) == False:
                    while True:
                        print("zly ruch musisz podac jeszcze raz")
                        skad = input(int())
                        dokad = input(int())
                        x = self.convertToBoard(skad)
                        y = self.convertToBoard(dokad)
                        if self.move(x, y) == True:
                           break
                self.display_board()

    def getGame(self):
        return self.whitePlayer, self.blackPlayer, self.board

    def setGame(self, newWhitePlayer, newBlackPlayer, newBoard):
        self.whitePlayer = newWhitePlayer
        self.blackPlayer = newBlackPlayer
        self.board = newBoard
        return self.whitePlayer, self.blackPlayer, self.board


    def move(self, skad, dokad):
        if self.getPieceFromBoard(skad) is None:
            print("nie ma pionka na pozycji startujacej")
            return False
        return self.getCellFromBoard(skad).piece.move(skad, dokad)


    def czy(self, krol, kolorPionkowBijacych):
        self.krol = krol
        self.kolorPionkowBijacych = kolorPionkowBijacych
        pozycjaKrola = self.krol.currentPosition
        whitePieces = self.bialyPlayer.figury
        blackPieces = self.czarnyPlayer.figury
        if self.kolorPionkowBijacych == "w":
            for i in range(len(whitePieces)):
                if whitePieces[i] is not None:
                    self.x = whitePieces[i]
                    if self.x.move(self.x.currentPosition, pozycjaKrola) == True:
                        return True
            return False
        else:
            for i in range(len(blackPieces)):
                if blackPieces[i] is not None:
                    self.x = blackPieces[i]
                    if self.x.move(self.x.currentPosition, pozycjaKrola) == True:
                        return True
            return False

    def generateRandomMoveVerticalAndHorizontal(self):
        howManyField = random.randint(1, 7)
        direction = random.randint(1, 4)
        x1, y1 = self.wylosowanaFigura.currentPosition
        if direction == 1:
            destination = x1 + howManyField, y1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 2:
            destination = x1 - howManyField, y1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 3:
            destination = x1, y1 + howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 4:
            destination = x1, y1 - howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False

    def genarateRandomMoveSkosy(self):
        howManyField = random.randint(1, 7)
        direction = random.randint(1, 4)
        x1, y1 = self.wylosowanaFigura.currentPosition
        if direction == 1:
            destination = x1 + howManyField, y1 + howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 2:
            destination = x1 - howManyField, y1 + howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 3:
            destination = x1 + howManyField, y1 - howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 4:
            destination = x1 - howManyField, y1 - howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False

    def generateMoveToKing(self):
        direction = random.randint(1, 8)
        x1, y1 = self.wylosowanaFigura.currentPosition
        if direction == 1:
            destination = x1+1, y1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 2:
            destination = x1+1, y1+1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 3:
            destination = x1+1, y1-1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 4:
            destination = x1, y1-1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 5:
            destination = x1-1, y1-1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 6:
            destination = x1-1, y1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 7:
            destination = x1-1, y1+1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 8:
            destination = x1, y1+1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False

    def generateMoveToKnight(self):
        direction = random.randint(1, 8)
        x1, y1 = self.wylosowanaFigura.currentPosition
        if direction == 1:
            destination = x1+2, y1-1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 2:
            destination = x1+2, y1+1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction ==3:
            destination = x1-2, y1+1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction == 4:
            destination = x1-2, y1-1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction ==5:
            destination = x1+1, y1-2
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction ==6:
            destination = x1-1, y1-2
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction ==7:
            destination = x1 -1, y1+2
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False
        elif direction ==8:
            destination = x1+1, y1+2
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                return True
            else:
                return False

    def generateMoveToPawn(self,piece):
        x, y = self.wylosowanaFigura.currentPosition
        self.piece = piece
        if self.wylosowanaFigura.color == "w":
            if self.wylosowanaFigura.currentPosition[0] == 6:
                if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (x-2,y)) == True:
                    return True
                else:
                    return False
            elif self.wylosowanaFigura.currentPosition[0] == 1:
                self.pawnPromotion(self.wylosowanaFigura.currentPosition,piece)
                return True
            else:
                if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (x-1,y)) == True:
                    return True
                else:
                    return False
        else:
            if self.wylosowanaFigura.currentPosition[0] == 1:
                if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (x+2,y)) == True:
                    return True
                else:
                    return False
            else:
                if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (x+1), y) == True:
                    return True
                else:
                    return False

    def pawnPromotion(self, position, piece):
        if self.getColorFromBoard(position) == "w" and piece.currentPosition[0] == 1:
            x,y=position
            x=x-1
            position = x, y
            self.removeFromWhiteList(piece) # usuwamy z tej listy
            piece.remove_piece(piece.currentPosition) # usuwanie z planszy
            if not hasattr(self, 'q3'):
                q3 = None
                self.creatingNewQueen(q3,position,"w")
                return True
            elif not hasattr(self, 'q4'):
                q4 = None
                self.creatingNewQueen(q4,position,"w")
                return True
            elif not hasattr(self, 'q5'):
                q5 = None
                self.creatingNewQueen(q5, position,"w")
                return True
            elif not hasattr(self, 'q6'):
                q6 = None
                self.creatingNewQueen(q6, position, "w")
                return True
            elif not hasattr(self, 'q7'):
                q7 = None
                self.creatingNewQueen(q7,position, "w")
                return True
            elif not hasattr(self, 'q8'):
                q8 = None
                self.creatingNewQueen(q8, position, "w")
                return True
        elif self.colorAi == "b" and piece.currentPosition[0] == 7:
            self.removing(piece)
            piece.remove_piece(piece.currentPosition)  # usuwanie z planszy
            if not hasattr(self, 'q9'):
                q9 = None
                self.creatingNewQueen(q9,position,"b")
                return True
            elif not hasattr(self, 'q10'):
                q10 = None
                self.creatingNewQueen(q10,position,"b")
                return True
            elif not hasattr(self, 'q11'):
                q11 = None
                self.creatingNewQueen(q11, position,"b")
                return True
            elif not hasattr(self, 'q12'):
                q12 = None
                self.creatingNewQueen(q12, position, "b")
                return True
            elif not hasattr(self, 'q13'):
                q13 = None
                self.creatingNewQueen(q13,position, "b")
                return True
            elif not hasattr(self, 'q14'):
                q14 = None
                self.creatingNewQueen(q14, position, "b")
                return True
        else:
            print("no cos tu nie dziala no")
            return False

    def creatingNewQueen(self, obiekt, position,color):
        self.obiekt = obiekt
        obiekt = Queen(position,color,self.szachownica)
        self.place_piece(obiekt,position)
        self.bialyPlayer.addFigury(obiekt)
        return obiekt



    def whatColorAi(self, colorAi):
        self.colorAi = colorAi
        return self.colorAi

    def moveAi(self):
        if self.colorAi == "w":
            if self.czy(self.k1, "w") == False:
                piece =self.r3.checkKillsVertical(self.r3.currentPosition)
                if piece != False: #czyli zabilo
                    self.removing(piece)
                    return True
                piece = self.r3.checkKillsChorizontal(self.r3.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.r4.checkKillsVertical(self.r4.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.r4.checkKillsChorizontal(self.r4.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.b3.checkKillsSkosy(self.b3.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.b4.checkKillsSkosy(self.b4.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.q2.checkKillsSkosy(self.q2.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.q2.checkKillsChorizontal(self.q2.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.q2.checkKillsVertical(self.q2.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.k2.checkKillsOneField(self.k2.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.n3.checkKillsKnight(self.n3.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.n4.checkKillsKnight(self.n4.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.p9.checkKillsOneFieldSkosy(self.p9.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.p10.checkKillsOneFieldSkosy(self.p10.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece =  self.p11.checkKillsOneFieldSkosy(self.p11.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.p12.checkKillsOneFieldSkosy(self.p12.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.p13.checkKillsOneFieldSkosy(self.p13.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece =self.p14.checkKillsOneFieldSkosy(self.p14.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece =  self.p15.checkKillsOneFieldSkosy(self.p15.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                piece = self.p16.checkKillsOneFieldSkosy(self.p16.currentPosition)
                if piece != False:
                    self.removing(piece)
                    return True
                else:
                    wylosowanaFigura = self.randomWhitePieceFromBoard()
                    self.wylosowanaFigura = wylosowanaFigura
                    if wylosowanaFigura.type == "wr":
                        if self.generateRandomMoveVerticalAndHorizontal() == True:
                            return True
                        else:
                            self.moveAi()
                    elif wylosowanaFigura.type == "wb":
                        if self.genarateRandomMoveSkosy() == True:
                            return True
                        else:
                            self.moveAi()
                    elif wylosowanaFigura.type == "wq":
                        if self.genarateRandomMoveSkosy() == True or self.generateRandomMoveVerticalAndHorizontal() == True:
                            return True
                        else:
                            self.moveAi()
                    elif wylosowanaFigura.type == "wk":
                        if self.generateMoveToKing() == True:
                            return True
                        else:
                            self.moveAi()
                    elif wylosowanaFigura.type == "wp":
                        if self.generateMoveToPawn(wylosowanaFigura) == True:
                            return True
                        else:
                            self.moveAi()
                    elif wylosowanaFigura.type == "wn":
                        print("jest kooooon")
                        if self.generateMoveToKnight()==True:
                            return True
                        else:
                            self.moveAi()
            else:
                print("szachujemy krola  chyba szach mat?????????")
                print("KONIEC GRY")

            return False





##SPR CZY MOJ KROL NIE JEST SZACHOWANY CZYLI CHYBA CZY NIE JEST SZACH? czy jest zagrozony
                #jesli jest to musze nim uciekac
                #if nie ma pata czyli jesli jest jakikolwiek dozwolony ruch


