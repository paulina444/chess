from board import *
from cell import *
import random
class Game(Board):
    def __init__(self):
        #self.color = color
        super().__init__()


#TODO dokoczyc szach mata dla drugiego koloru
#dokonczyc movaai dla drugiego koloru


#roszade
#zmienic na angielski ladnie
#skorcic do ladnych metod ;)
#to pawn promotion tam wez ogarnij
#jesli wpisze cos zlego do terminala? to sie wywala
#gdy wybieram nie swoj kolor w move



    def play(self):
        self.nextmove = None
        if self.nextmove == None:
            colorAi = "w"
            self.whatColorAi(colorAi)
        else:
            colorAi = "b"
            self.whatColorAi(colorAi)
        while True:
            if colorAi == "w":

                self.moveAi()

                self.display_board()
                print("Graczu, podaj, gdzie chcesz się ruszyć (w formacie a5-a6):")
                ruch = input()
                skad, dokad = ruch.split('-')
                x = self.convertToBoard(skad)
                y = self.convertToBoard(dokad)


                if self.move(x,y) == False:
                    while True:
                        print("zly ruch musisz podac jeszcze raz")
                        ruch = input()
                        skad, dokad = ruch.split('-')
                        x = self.convertToBoard(skad)
                        y = self.convertToBoard(dokad)
                        move = self.move(x, y)
                        if move == True or move == "kill":
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
        color = self.getColorFromBoard(skad)
        if self.isKingUnderAttack(color) == True:
            print("UWAGA KROL POD BICIEM")
            if self.getPieceFromBoard(dokad) is not None:
                self.pieceToDelete = self.getPieceFromBoard(dokad)
                self.opponentColor = self.getColorFromBoard(dokad)
            move = self.getCellFromBoard(skad).piece.move(skad, dokad)
            if move == True or move == "kill":
                if self.isKingUnderAttack(color) == True:

                    if self.getCellFromBoard(dokad).getPiece().type == "wp":
                        self.getCellFromBoard(dokad).piece.move_base(skad)
                        print("szach? musisz uratowac swojego krola")
                        return False
                    elif self.getCellFromBoard(dokad).getPiece().type == "bp":
                        self.getCellFromBoard(dokad).piece.move_base(skad)
                        print("szach? musisz uratowac swojego krola")
                        return False
                    else:
                        self.getCellFromBoard(dokad).piece.move(dokad,skad)
                        print("szach? mussiz ratowac swojego krola")
                        return False
                else:
                    if move == "kill":
                        if self.opponentColor == "w":
                            self.removeFromWhiteList(self.pieceToDelete)
                            return True
                        else:
                            self.removing(self.pieceToDelete)
                    color = self.getColorFromBoard(dokad)
                    if self.isOpponentMated(color) == True:
                        print("MATTTTTTTTTTTTTTTTTTTTTT I KONIEC GRY")

                    print("uf uciekl") #uciekl spr czy przeciwnikowi zrb mata jesli tak koniec gry
                    return True
            else:
                return False #tzn zrb zly ruch
        else:
            if self.getPieceFromBoard(dokad) is not None:
                piece = self.getPieceFromBoard(dokad)
                color = self.getColorFromBoard(dokad)
            myColor = self.getColorFromBoard(skad)
            move = self.getCellFromBoard(skad).piece.move(skad, dokad)
            #tutaj ze po movie jesli king jest pod biciem... to
            if self.isKingUnderAttack(myColor) == True:

                if self.getCellFromBoard(dokad).getPiece().type == "wp":
                    self.getCellFromBoard(dokad).piece.move_base(skad)
                    print("szach? musisz uratowac swojego krola")
                    return False
                elif self.getCellFromBoard(dokad).getPiece().type == "bp":
                    self.getCellFromBoard(dokad).piece.move_base(skad)
                    print("szach? musisz uratowac swojego krola")
                    return False
                else:
                    self.getCellFromBoard(dokad).piece.move(dokad, skad)
                    print("szach? mussiz ratowac swojego krola")
                    return False
            if self.isOpponentMated(color) == True: #spr czy matujemy przeciwnika
                print("MATTTTTTTTTTTTTTTTTTTTTT I KONIEC GRY")
            if move == "kill":
                if color == "w":
                    self.removeFromWhiteList(piece)
                    return True
                else:
                    self.removing(piece)
                    return True
            elif move == False:
                return False
            else:
                return True

    def isOpponentMated(self,color):
        if self.isKingUnderAttack(color) == True:
            if self.isCheckMate(color) == True:
                return True #MATOWIMY PRZECIWNIKA I KONIEC GRY
        return False

    def isKingUnderAttack(self, color):
        whitePieces = self.bialyPlayer.figury
        blackPieces = self.czarnyPlayer.figury
        if color == "w":
            kingPosition = self.k2.currentPosition
            for i in range(len(blackPieces)):
                if blackPieces[i] is not None:
                    self.blackPiece = blackPieces[i]
                    if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, kingPosition) == "kill":
                        self.attackerPosition = self.blackPiece.currentPosition
                        self.attacker = self.blackPiece
                        print("UWAGA KROL POD ATAKIEM")
                        return True
            return False
        elif color == "b":
            kingPosition = self.k1.currentPosition
            for i in range(len(whitePieces)):
                if whitePieces[i] is not None:
                    self.whitePiece = whitePieces[i]
                    if self.whitePiece.isValidateMove(self.whitePiece.currentPosition, kingPosition) == "kill":
                        self.attackerPosition = self.whitePiece.currentPosition
                        self.attacker = self.whitePiece
                        print("UWAGA KROL POD ATAKIEM")
                        return True
            return False

    def isCheckMate(self, kingColor):
        whitePieces = self.bialyPlayer.figury
        blackPieces = self.czarnyPlayer.figury
        if kingColor == "w":
            kingPosition = self.k2.currentPosition #spr czy bialy moze zabic atakujacego
            for i in range(len(whitePieces)):
                if whitePieces[i] is not None:
                    self.whitePiece = whitePieces[i]
                    if self.whitePiece.isValidateMove(self.whitePiece.currentPosition,self.attackerPosition) == "kill":
                        return False #nie ma szacha mata bo mozna zabic atakera

            #spr czy king moze sam uciec
            king = self.k2
            if self.isValidateEscapeToKing(king, king.currentPosition, king.color) == True:
                return False  # moze uciec to nie ma mata

            """if self.k2.isValidateMove(kingPosition,(kingPosition[0]+1,kingPosition[1])) == True:
                if self.isKingUnderAttack("w") == False:
                    return False #bo moze sie ukryc king
            if self.k2.isValidateMove(kingPosition,(kingPosition[0]-1,kingPosition[1])) == True:
                if self.isKingUnderAttack("w") == False:
                    return False #bo moze sie ukryc king
            if self.k2.isValidateMove(kingPosition,(kingPosition[0],kingPosition[1]+1)) == True:
                if self.isKingUnderAttack("w") == False:
                    return False #bo moze sie ukryc king
            if self.k2.isValidateMove(kingPosition,(kingPosition[0],kingPosition[1]-1)) == True:
                if self.isKingUnderAttack("w") == False:
                    return False #bo moze sie ukryc king
            if self.k2.isValidateMove(kingPosition,(kingPosition[0]+1,kingPosition[1]+1)) == True:
                if self.isKingUnderAttack("w") == False:
                    return False #bo moze sie ukryc king
            if self.k2.isValidateMove(kingPosition,(kingPosition[0]-1,kingPosition[1]-1)) == True:
                if self.isKingUnderAttack("w") == False:
                    return False #bo moze sie ukryc king
            if self.k2.isValidateMove(kingPosition,(kingPosition[0]+1,kingPosition[1]-1)) == True:
                if self.isKingUnderAttack("w") == False:
                    return False #bo moze sie ukryc king
            if self.k2.isValidateMove(kingPosition,(kingPosition[0]-1,kingPosition[1]+1)) == True:
                if self.isKingUnderAttack("w") == False:
                    return False #bo moze sie ukryc king"""


            #tutaj jeszcze trzeba spr czy atakujaca figura nie jest koniem bo jesli jest to nic nie da wejscie pomiedzy nia
            if self.attacker.type != "bn":
                x, y = kingPosition
                x1, y1 = self.attackerPosition
                length_x = abs(x1 - x)
                length_y = abs(y1 - y)

                if x > x1 and y == y1:  # od dolu na pawo
                    for i in range(x1 + 1, x):
                        position = i, y1
                        #teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(whitePieces)):
                            if whitePieces[i] is not None:
                                self.whitePiece = whitePieces[i]
                                if self.whitePiece.isValidateMove(self.whitePiece.currentPosition, position) == True:
                                    return False #to nie ma bicia
                elif x<x1 and y==y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        #teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(whitePieces)):
                            if whitePieces[i] is not None:
                                self.whitePiece = whitePieces[i]
                                if self.whitePiece.isValidateMove(self.whitePiece.currentPosition, position) == True:
                                    return False #to nie ma bicia
                elif y>y1 and x==x1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        #teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(whitePieces)):
                            if whitePieces[i] is not None:
                                self.whitePiece = whitePieces[i]
                                if self.whitePiece.isValidateMove(self.whitePiece.currentPosition, position) == True:
                                    return False #to nie ma bicia
                elif y<y1 and x==x1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        #teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(whitePieces)):
                            if whitePieces[i] is not None:
                                self.whitePiece = whitePieces[i]
                                if self.whitePiece.isValidateMove(self.whitePiece.currentPosition, position) == True:
                                    return False #to nie ma bicia

                elif x>x1 and y>y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        #teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(whitePieces)):
                            if whitePieces[i] is not None:
                                self.whitePiece = whitePieces[i]
                                if self.whitePiece.isValidateMove(self.whitePiece.currentPosition, position) == True:
                                    return False #to nie ma bicia
                elif x<x1 and y<y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        #teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(whitePieces)):
                            if whitePieces[i] is not None:
                                self.whitePiece = whitePieces[i]
                                if self.whitePiece.isValidateMove(self.whitePiece.currentPosition, position) == True:
                                    return False #to nie ma bicia
                elif x>x1 and y<y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        #teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(whitePieces)):
                            if whitePieces[i] is not None:
                                self.whitePiece = whitePieces[i]
                                if self.whitePiece.isValidateMove(self.whitePiece.currentPosition, position) == True:
                                    return False #to nie ma bicia
                elif x<x1 and y>y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        #teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(whitePieces)):
                            if whitePieces[i] is not None:
                                self.whitePiece = whitePieces[i]
                                if self.whitePiece.isValidateMove(self.whitePiece.currentPosition, position) == True:
                                    return False #to nie ma bicia

            return True #SZACH MAT JEST WTEDY
        else:
            kingPosition = self.k1.currentPosition  # spr czy czarny moze zabic atakujacego
            for i in range(len(blackPieces)):
                if blackPieces[i] is not None:
                    self.blackPiece = blackPieces[i]
                    if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, self.attackerPosition) == "kill":
                        return False  # nie ma szacha mata bo mozna zabic atakera
            # spr czy king moze sam uciec
            king = self.k1
            if self.isValidateEscapeToKing(king,king.currentPosition,king.color) == True:
                return False #moze uciec to nie ma mata


            # tutaj jeszcze trzeba spr czy atakujaca figura nie jest koniem bo jesli jest to nic nie da wejscie pomiedzy nia
            if self.attacker.type != "wn":
                x, y = kingPosition
                x1, y1 = self.attackerPosition
                length_x = abs(x1 - x)
                length_y = abs(y1 - y)

                if x > x1 and y == y1:  # od dolu na pawo
                    for i in range(x1 + 1, x):
                        position = i, y1
                        # teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(blackPieces)):
                            if whitePieces[i] is not None:
                                self.blackPiece = blackPieces[i]
                                if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, position) == True:
                                    return False  # to nie ma bicia
                elif x < x1 and y == y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        # teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(blackPieces)):
                            if blackPieces[i] is not None:
                                self.blackPiece = blackPieces[i]
                                if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, position) == True:
                                    return False  # to nie ma bicia
                elif y > y1 and x == x1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        # teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(blackPieces)):
                            if blackPieces[i] is not None:
                                self.blackPiece = blackPieces[i]
                                if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, position) == True:
                                    return False  # to nie ma bicia
                elif y < y1 and x == x1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        # teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(blackPieces)):
                            if blackPieces[i] is not None:
                                self.blackPiece = blackPieces[i]
                                if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, position) == True:
                                    return False  # to nie ma bicia

                elif x > x1 and y > y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        # teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(blackPieces)):
                            if blackPieces[i] is not None:
                                self.blackPiece = blackPieces[i]
                                if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, position) == True:
                                    return False  # to nie ma bicia
                elif x < x1 and y < y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        # teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(blackPieces)):
                            if blackPieces[i] is not None:
                                self.blackPiece = blackPieces[i]
                                if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, position) == True:
                                    return False  # to nie ma bicia
                elif x > x1 and y < y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        # teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(blackPieces)):
                            if blackPieces[i] is not None:
                                self.blackPiece = blackPieces[i]
                                if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, position) == True:
                                    return False  # to nie ma bicia
                elif x < x1 and y > y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        # teraz trzeba spr czy na ta pozycje moze pojsc jakas nasza figura
                        for i in range(len(blackPieces)):
                            if blackPieces[i] is not None:
                                self.blackPiece = blackPieces[i]
                                if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, position) == True:
                                    return False  # to nie ma bicia

            return True  # SZACH MAT JEST WTEDY

    def isValidateEscapeToKing(self, king, kingPosition, colorKing):
        if king.isValidateMove(kingPosition, (kingPosition[0] + 1, kingPosition[1])) == True:
            if self.isKingUnderAttack(colorKing) == False:
                return True  # bo moze sie ukryc king
        if king.isValidateMove(kingPosition, (kingPosition[0] - 1, kingPosition[1])) == True:
            if self.isKingUnderAttack(colorKing) == False:
                return True  # bo moze sie ukryc king
        if king.isValidateMove(kingPosition, (kingPosition[0], kingPosition[1] + 1)) == True:
            if self.isKingUnderAttack(colorKing) == False:
                return True  # bo moze sie ukryc king
        if king.isValidateMove(kingPosition, (kingPosition[0], kingPosition[1] - 1)) == True:
            if self.isKingUnderAttack(colorKing) == False:
                return True # bo moze sie ukryc king
        if king.isValidateMove(kingPosition, (kingPosition[0] + 1, kingPosition[1] + 1)) == True:
            if self.isKingUnderAttack(colorKing) == False:
                return True  # bo moze sie ukryc king
        if king.isValidateMove(kingPosition, (kingPosition[0] - 1, kingPosition[1] - 1)) == True:
            if self.isKingUnderAttack(colorKing) == False:
                return True  # bo moze sie ukryc king
        if king.isValidateMove(kingPosition, (kingPosition[0] + 1, kingPosition[1] - 1)) == True:
            if self.isKingUnderAttack(colorKing) == False:
                return True  # bo moze sie ukryc king
        if king.isValidateMove(kingPosition, (kingPosition[0] - 1, kingPosition[1] + 1)) == True:
            if self.isKingUnderAttack(colorKing) == False:
                return True  # bo moze sie ukryc king
        return False

    def generateRandomMoveVerticalAndHorizontal(self):
        howManyField = random.randint(1, 7)
        direction = random.randint(1, 4)
        x1, y1 = self.wylosowanaFigura.currentPosition
        start = self.wylosowanaFigura.currentPosition
        if direction == 1:
            destination = x1 + howManyField, y1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 2:
            destination = x1 - howManyField, y1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 3:
            destination = x1, y1 + howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 4:
            destination = x1, y1 - howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False

    def genarateRandomMoveSkosy(self):
        howManyField = random.randint(1, 7)
        direction = random.randint(1, 4)
        x1, y1 = self.wylosowanaFigura.currentPosition
        start = self.wylosowanaFigura.currentPosition
        if direction == 1:
            destination = x1 + howManyField, y1 + howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 2:
            destination = x1 - howManyField, y1 + howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 3:
            destination = x1 + howManyField, y1 - howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 4:
            destination = x1 - howManyField, y1 - howManyField
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False

    def generateMoveToKing(self):
        direction = random.randint(1, 8)
        x1, y1 = self.wylosowanaFigura.currentPosition
        start = self.wylosowanaFigura.currentPosition
        if direction == 1:
            destination = x1+1, y1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 2:
            destination = x1+1, y1+1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 3:
            destination = x1+1, y1-1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 4:
            destination = x1, y1-1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 5:
            destination = x1-1, y1-1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 6:
            destination = x1-1, y1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 7:
            destination = x1-1, y1+1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
        elif direction == 8:
            destination = x1, y1+1
            if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard(destination).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                return False
    def moveAndIsUnderAttackKing(self,start ,destination):
        if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (destination)) == True:
            if self.isKingUnderAttack(self.colorAi) == True:
                self.getCellFromBoard(destination).piece.move_base(start)
                return False
            else:
                return True
        else:
            return False
    def generateMoveToKnight(self):
        direction = random.randint(1, 8)
        x1, y1 = self.wylosowanaFigura.currentPosition
        start = self.wylosowanaFigura.currentPosition
        if direction == 1:
            destination = x1 + 2, y1 - 1
            if self.moveAndIsUnderAttackKing(start,destination) == True:
                return True
            return False
        elif direction == 2:
            destination = x1 + 2, y1 + 1
            if self.moveAndIsUnderAttackKing(start, destination) == True:
                return True
            return False
        elif direction == 3:
            destination = x1 - 2, y1 + 1
            if self.moveAndIsUnderAttackKing(start, destination) == True:
                return True
            return False
        elif direction == 4:
            destination = x1 - 2, y1 - 1
            if self.moveAndIsUnderAttackKing(start, destination) == True:
                return True
            return False
        elif direction == 5:
            destination = x1 + 1, y1 - 2
            if self.moveAndIsUnderAttackKing(start, destination) == True:
                return True
            return False
        elif direction == 6:
            destination = x1-1, y1 - 2
            if self.moveAndIsUnderAttackKing(start, destination) == True:
                return True
            return False
        elif direction == 7:
            destination = x1 -1, y1 + 2
            if self.moveAndIsUnderAttackKing(start, destination) == True:
                return True
            return False
        elif direction == 8:
            destination = x1+1, y1 + 2
            if self.moveAndIsUnderAttackKing(start, destination) == True:
                return True
            return False

    def generateMoveToPawn(self,piece):
        x, y = self.wylosowanaFigura.currentPosition
        start = self.wylosowanaFigura.currentPosition
        self.piece = piece
        if self.wylosowanaFigura.color == "w":
            if self.wylosowanaFigura.currentPosition[0] == 6:
                if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (x-2,y)) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        self.getCellFromBoard((x-2,y)).piece.move_base(start)
                        return False
                    else:
                        return True
                else:
                    return False
            elif self.wylosowanaFigura.currentPosition[0] == 1:
                self.pawnPromotion(self.wylosowanaFigura.currentPosition,piece)
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard((x-1,y)).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (x-1,y)) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        self.getCellFromBoard((x-1,y)).piece.move_base(start)
                        return False
                    else:
                        return True
                else:
                    return False
        else:
            if self.wylosowanaFigura.currentPosition[0] == 1:
                if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (x+2,y)) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        self.getCellFromBoard((x+2,y)).piece.move_base(start)
                        return False
                    else:
                        return True
                else:
                    return False
            elif self.wylosowanaFigura.currentPosition[0] == 6:
                self.pawnPromotion(self.wylosowanaFigura.currentPosition,piece)
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard((x+1,y)).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                if self.wylosowanaFigura.move((self.wylosowanaFigura.currentPosition), (x+1), y) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        self.getCellFromBoard((x+1,y)).piece.move_base(start)
                        return False
                    else:
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
            return False

    def creatingNewQueen(self, queen, position,color):
        self.queen = queen
        queen = Queen(position,color,self.szachownica)
        self.place_piece(queen,position)
        self.bialyPlayer.addFigury(queen)
        return queen

    def whatColorAi(self, colorAi):
        self.colorAi = colorAi
        return self.colorAi

    def moveAi(self):
        if self.colorAi == "w":
            whitePieces = self.bialyPlayer.figury
            for i in range(len(whitePieces)):
                if whitePieces[i] is not None:
                    self.piece = whitePieces[i]
                    start = self.piece.currentPosition
                    if self.piece.checkKills(self.piece.currentPosition) == True:
                        if self.isKingUnderAttack(self.colorAi) == True:
                            end = self.piece.currentPosition
                            self.getCellFromBoard(end).piece.move_base(start)
                            self.moveAi()
                        else:
                            print("BIJE")
                            if self.isOpponentMated("b") == True:
                                print("MATTTTTTTTTTTTTTTTTTTTTT I KONIEC GRY")
                            return True
            wylosowanaFigura = self.randomWhitePieceFromBoard()
            self.wylosowanaFigura = wylosowanaFigura
            if wylosowanaFigura.type == "wr":
                if self.generateRandomMoveVerticalAndHorizontal() == True:
                    print("robie move")
                    if self.isOpponentMated("b") == True:
                        print("MATTTTTTTTTTTTTTTTTTTTTT I KONIEC GRY")
                    return True
                else:
                    self.moveAi()
            elif wylosowanaFigura.type == "wb":
                if self.genarateRandomMoveSkosy() == True:
                    print("robie move")
                    if self.isOpponentMated("b") == True:
                        print("MATTTTTTTTTTTTTTTTTTTTTT I KONIEC GRY")
                    return True
                else:
                    self.moveAi()
            elif wylosowanaFigura.type == "wq":
                if self.genarateRandomMoveSkosy() == True or self.generateRandomMoveVerticalAndHorizontal() == True:
                    print("robie move")
                    if self.isOpponentMated("b") == True:
                        print("MATTTTTTTTTTTTTTTTTTTTTT I KONIEC GRY")
                    return True
                else:
                    self.moveAi()
            elif wylosowanaFigura.type == "wk":
                if self.generateMoveToKing() == True:
                    print("robie move")
                    if self.isOpponentMated("b") == True:
                        print("MATTTTTTTTTTTTTTTTTTTTTT I KONIEC GRY")
                    return True
                else:
                    self.moveAi()
            elif wylosowanaFigura.type == "wp":
                if self.generateMoveToPawn(wylosowanaFigura) == True:
                    print("robie move")
                    if self.isOpponentMated("b") == True:
                        print("MATTTTTTTTTTTTTTTTTTTTTT I KONIEC GRY")
                    return True
                else:
                    self.moveAi()
            elif wylosowanaFigura.type == "wn":
                if self.generateMoveToKnight()==True:
                    print("robie move")
                    if self.isOpponentMated("b") == True:
                        print("MATTTTTTTTTTTTTTTTTTTTTT I KONIEC GRY")
                    return True
                else:
                    self.moveAi()

            return False





