from game import *
class Ai(Game):
    def generateRandomMoveVerticalAndHorizontal(self):
        howManyField = random.randint(1, 7)
        direction = random.randint(1, 4)
        x1, y1 = self.randomPiece.currentPosition
        start = self.randomPiece.currentPosition

        if direction == 1:
            self.destination = x1 + howManyField, y1
        elif direction == 2:
            self.destination = x1 - howManyField, y1
        elif direction == 3:
            self.destination = x1, y1 + howManyField
        elif direction == 4:
            self.destination = x1, y1 - howManyField

        if self.randomPiece.move(self.randomPiece.currentPosition, self.destination) == True:
            if self.isKingUnderAttack(self.colorAi) == True:
                self.getCellFromBoard(self.destination).piece.move_base(start)
                return False
            else:
                return True
        else:
            return False

    def genarateRandomMoveDiagonal(self):
        howManyField = random.randint(1, 7)
        direction = random.randint(1, 4)
        x1, y1 = self.randomPiece.currentPosition
        start = self.randomPiece.currentPosition
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

        destination = x1 + directions[direction - 1][0] * howManyField, y1 + directions[direction - 1][1] * howManyField
        if self.randomPiece.move(self.randomPiece.currentPosition, destination) == True:
            if self.isKingUnderAttack(self.colorAi) == True:
                self.getCellFromBoard(destination).piece.move_base(start)
                return False
            else:
                return True
        else:
            return False

    def generateMoveToKing(self):
        direction = random.randint(1, 8)
        x1, y1 = self.randomPiece.currentPosition
        start = self.randomPiece.currentPosition
        directions = [(1, 0), (1, 1), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

        for i in range(8):
            if direction == i + 1:
                destination = x1 + directions[i][0], y1 + directions[i][1]
                if self.randomPiece.move(self.randomPiece.currentPosition, destination) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        self.getCellFromBoard(destination).piece.move_base(start)
                        return False
                    else:
                        return True
                else:
                    return False
        return False

    def moveAndIsUnderAttackKing(self,start ,destination):
        if self.randomPiece.move((self.randomPiece.currentPosition), (destination)) == True:
            if self.isKingUnderAttack(self.colorAi) == True:
                self.getCellFromBoard(destination).piece.move_base(start)
                return False
            else:
                return True
        else:
            return False

    def generateMoveToKnight(self):
        direction = random.randint(1, 8)
        x1, y1 = self.randomPiece.currentPosition
        start = self.randomPiece.currentPosition
        directions = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, -2), (-1, -2), (-1, 2), (1, 2)]

        for i in range(8):
            if direction == i + 1:
                destination = x1 + directions[i][0], y1 + directions[i][1]
                if self.moveAndIsUnderAttackKing(start, destination) == True:
                    return True
                return False
        return False

    def generateMoveToPawn(self,piece):
        x, y = self.randomPiece.currentPosition
        start = self.randomPiece.currentPosition
        self.piece = piece
        if self.randomPiece.color == "w":
            if self.randomPiece.currentPosition[0] == 6:
                if self.randomPiece.move((self.randomPiece.currentPosition), (x-2,y)) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        self.getCellFromBoard((x-2,y)).piece.move_base(start)
                        return False
                    else:
                        return True
                else:
                    return False
            elif self.randomPiece.currentPosition[0] == 1:
                self.pawnPromotion(self.randomPiece.currentPosition,piece)
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard((x-1,y)).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                if self.randomPiece.move((self.randomPiece.currentPosition), (x-1,y)) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        self.getCellFromBoard((x-1,y)).piece.move_base(start)
                        return False
                    else:
                        return True
                else:
                    return False
        else:
            if self.randomPiece.currentPosition[0] == 1:
                if self.randomPiece.move((self.randomPiece.currentPosition), (x+2,y)) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        self.getCellFromBoard((x+2,y)).piece.move_base(start)
                        return False
                    else:
                        return True
                else:
                    return False
            elif self.randomPiece.currentPosition[0] == 6:
                self.pawnPromotion(self.randomPiece.currentPosition,piece)
                if self.isKingUnderAttack(self.colorAi) == True:
                    self.getCellFromBoard((x+1,y)).piece.move_base(start)
                    return False
                else:
                    return True
            else:
                if self.randomPiece.move((self.randomPiece.currentPosition), (x+1,y)) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        self.getCellFromBoard((x+1,y)).piece.move_base(start)
                        return False
                    else:
                        return True
                else:
                    return False

    def moveAi(self):
        if self.colorAi == "w":
            self.Pieces = self.whitePlayer.figury
            self.opponent = "b"
            randomPiece = self.randomWhitePieceFromBoard()
            self.randomPiece = randomPiece
        else:
            self.Pieces = self.blackPlayer.figury
            self.opponent = "w"
            randomPiece = self.randomBlackPieceFromBoard()
            self.randomPiece = randomPiece

        for i in range(len(self.Pieces)):
            if self.Pieces[i] is not None:
                self.piece = self.Pieces[i]
                start = self.piece.currentPosition
                if self.piece.checkKills(self.piece.currentPosition) == True:
                    if self.isKingUnderAttack(self.colorAi) == True:
                        end = self.piece.currentPosition
                        self.getCellFromBoard(end).piece.move_base(start)
                        self.moveAi()
                    else:
                        print("BIJE")
                        if self.isOpponentMated(self.opponent) == True:
                            print("MAT I KONIEC GRY")
                            quit()
                        return True
        if randomPiece.type[1] == "r":
            if self.generateRandomMoveVerticalAndHorizontal() == True:
                print("robie move")
                if self.isOpponentMated(self.opponent) == True:
                    print("MAT I KONIEC GRY")
                    quit()
                return True
            else:
                self.moveAi()
        elif randomPiece.type[1] == "b":
            if self.genarateRandomMoveDiagonal() == True:
                print("robie ruch")
                if self.isOpponentMated(self.opponent) == True:
                    print("MAT I KONIEC GRY")
                    quit()
                return True
            else:
                self.moveAi()
        elif randomPiece.type[1] == "q":
            if self.genarateRandomMoveDiagonal() == True or self.generateRandomMoveVerticalAndHorizontal() == True:
                print("robie ruch")
                if self.isOpponentMated(self.opponent) == True:
                    print("MAT I KONIEC GRY")
                    quit()
                return True
            else:
                self.moveAi()
        elif randomPiece.type[1] == "k":
            if self.generateMoveToKing() == True:
                print("robie ruch")
                if self.isOpponentMated(self.opponent) == True:
                    print("MAT I KONIEC GRY")
                    quit()
                return True
            else:
                self.moveAi()
        elif randomPiece.type[1] == "p":
            if self.generateMoveToPawn(randomPiece) == True:
                print("robie ruch")
                if self.isOpponentMated(self.opponent) == True:
                    print("MAT I KONIEC GRY")
                    quit()
                return True
            else:
                self.moveAi()
        elif randomPiece.type[1] == "n":
            if self.generateMoveToKnight()==True:
                print("robie ruch")
                if self.isOpponentMated(self.opponent) == True:
                    print("MAT I KONIEC GRY")
                    quit()
                return True
            else:
                self.moveAi()

        return False