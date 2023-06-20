from board import *
from cell import *
import random
class Game(Board):
    def __init__(self):
        #self.color = color
        super().__init__()

    def getGame(self):
        return self.whitePlayer, self.blackPlayer, self.board

    def setGame(self, newWhitePlayer, newBlackPlayer, newBoard):
        self.whitePlayer = newWhitePlayer
        self.blackPlayer = newBlackPlayer
        self.board = newBoard
        return self.whitePlayer, self.blackPlayer, self.board

    def move(self, start, end):
        if self.getPieceFromBoard(start) is None:
            print("nie ma pionka na pozycji startujacej")
            return False
        if self.getColorFromBoard(start) == self.colorAi:
            return False
        color = self.getColorFromBoard(start)
        if self.isKingUnderAttack(color) == True:
            print("UWAGA KROL POD BICIEM")
            if self.getPieceFromBoard(end) is not None:
                self.pieceToDelete = self.getPieceFromBoard(end)
                self.opponentColor = self.getColorFromBoard(end)
            move = self.getCellFromBoard(start).piece.move(start, end)
            if move == True or move == "kill":
                if self.isKingUnderAttack(color) == True:
                    if self.getCellFromBoard(end).getPiece().type == "wp":
                        self.getCellFromBoard(end).piece.move_base(start)
                        print("szach? musisz uratowac swojego krola")
                        return False
                    elif self.getCellFromBoard(end).getPiece().type == "bp":
                        self.getCellFromBoard(end).piece.move_base(start)
                        print("szach? musisz uratowac swojego krola")
                        return False
                    else:
                        self.getCellFromBoard(end).piece.move(end,start)
                        print("szach? musisz ratowac swojego krola")
                        return False
                else:
                    if move == "kill":
                        if self.opponentColor == "w":
                            self.removeFromWhiteList(self.pieceToDelete)
                            return True
                        else:
                            self.removing(self.pieceToDelete)
                    color = self.getColorFromBoard(end)
                    if self.isOpponentMated(color) == True:
                        print("MAT I KONIEC GRY")
                        quit()

                    print("uf uciekl")
                    return True
            else:
                return False
        else:
            if self.getPieceFromBoard(end) is not None:
                self.pieceEnd = self.getPieceFromBoard(end)
                color = self.getColorFromBoard(end)
            myColor = self.getColorFromBoard(start)
            move = self.getCellFromBoard(start).piece.move(start, end)
            #tutaj ze po movie jesli king jest pod biciem... to
            if self.isKingUnderAttack(myColor) == True:

                if self.getCellFromBoard(end).getPiece().type == "wp":
                    self.getCellFromBoard(end).piece.move_base(start)
                    print("szach? musisz uratowac swojego krola")
                    return False
                elif self.getCellFromBoard(end).getPiece().type == "bp":
                    self.getCellFromBoard(end).piece.move_base(start)
                    print("szach? musisz uratowac swojego krola")
                    return False
                else:
                    self.getCellFromBoard(end).piece.move(end, start)
                    print("szach? mussiz ratowac swojego krola")
                    return False
            if self.isOpponentMated(color) == True:
                print("MAT I KONIEC GRY")
                quit()
            if move == "kill":
                if color == "w":
                    self.removeFromWhiteList(self.pieceEnd)
                    return True
                else:
                    self.removing(self.pieceEnd)
                    return True
            elif move == False:
                return False
            else:
                return True

    def isOpponentMated(self,color):
        if self.isKingUnderAttack(color) == True:
            if self.isCheckMate(color) == True:
                return True
        return False

    def isKingUnderAttack(self, color):
        whitePieces = self.whitePlayer.figury
        blackPieces = self.blackPlayer.figury
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

    def isValidateMoveToRangeOfPosition(self,position,colorDefendingPieces):
        if colorDefendingPieces == "b":
            piecesColor = self.blackPlayer.figury
        else:
            piecesColor = self.whitePlayer.figury
        for j in range(len(piecesColor)):
            if piecesColor[j] is not None:
                self.piece = piecesColor[j]
                if self.piece.isValidateMove(self.piece.currentPosition, position) == True:
                    if self.isKingUnderAttack(colorDefendingPieces) == False:
                        return True
        return False

    def isCheckMate(self, kingColor):
        whitePieces = self.whitePlayer.figury
        blackPieces = self.blackPlayer.figury
        if kingColor == "w":
            kingPosition = self.k2.currentPosition
            #spr mozna zabic atakujacego
            for i in range(len(whitePieces)):
                if whitePieces[i] is not None:
                    self.whitePiece = whitePieces[i]
                    if self.whitePiece.isValidateMove(self.whitePiece.currentPosition,self.attackerPosition) == "kill":
                        return False

            king = self.k2
            if self.isValidateEscapeToKing(king, king.currentPosition, king.color) == True:
                return False
            #spr czy na ta pozycje moze pojsc jakas nasza figura
            if self.attacker.type != "bn":
                x, y = kingPosition
                x1, y1 = self.attackerPosition

                if x > x1 and y == y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        if self.isValidateMoveToRangeOfPosition(position, "w") == True:
                            return False
                elif x < x1 and y == y1:
                    for i in range(x + 1, x1):
                        position = i, y1
                        if self.isValidateMoveToRangeOfPosition(position, "w") == True:
                            return False
                elif y > y1 and x == x1:
                    for i in range(y1 + 1, y):
                        position = x1, i
                        if self.isValidateMoveToRangeOfPosition(position, "w") == True:
                            return False
                elif y < y1 and x == x1:
                    for i in range(y + 1, y1):
                        position = x1, i
                        if self.isValidateMoveToRangeOfPosition(position, "w") == True:
                            return False
                elif x > x1 and y > y1:
                    for i in range(x1 + 1, x):
                        y1 = y1 + 1
                        position = i, y1
                        if self.isValidateMoveToRangeOfPosition(position, "w") == True:
                            return False
                elif x < x1 and y < y1:
                    for i in range(x + 1, x1):
                        y = y + 1
                        position = i, y
                        if self.isValidateMoveToRangeOfPosition(position, "w") == True:
                            return False
                elif x > x1 and y < y1:
                    for i in range(x1 + 1, x):
                        y = y + 1
                        position = i, y
                        if self.isValidateMoveToRangeOfPosition(position, "w") == True:
                            return False
                elif x < x1 and y > y1:
                    for i in range(x + 1, x1):
                        y1 = y1 + 1
                        position = i, y1
                        if self.isValidateMoveToRangeOfPosition(position, "w") == True:
                            return False
            return True
        else:
            kingPosition = self.k1.currentPosition
            for i in range(len(blackPieces)):
                if blackPieces[i] is not None:
                    self.blackPiece = blackPieces[i]
                    if self.blackPiece.isValidateMove(self.blackPiece.currentPosition, self.attackerPosition) == "kill":
                        return False
            king = self.k1
            if self.isValidateEscapeToKing(king,king.currentPosition,king.color) == True:
                return False

            if self.attacker.type != "wn":
                x, y = kingPosition
                x1, y1 = self.attackerPosition
                if x > x1 and y == y1:
                    for i in range(x1 + 1, x):
                        position = i, y1
                        if self.isValidateMoveToRangeOfPosition(position, "b") == True:
                            return False
                elif x < x1 and y == y1:
                    for i in range(x + 1, x1):
                        position = i, y1
                        if self.isValidateMoveToRangeOfPosition(position, "b") == True:
                            return False
                elif y > y1 and x == x1:
                    for i in range(y1 + 1, y):
                        position = x1, i
                        if self.isValidateMoveToRangeOfPosition(position, "b") == True:
                            return False
                elif y < y1 and x == x1:
                    for i in range(y + 1, y1):
                        position = x1, i
                        if self.isValidateMoveToRangeOfPosition(position, "b") == True:
                            return False
                elif x > x1 and y > y1:
                    for i in range(x1 + 1, x):
                        y1 = y1 + 1
                        position = i, y1
                        if self.isValidateMoveToRangeOfPosition(position, "b") == True:
                            return False
                elif x < x1 and y < y1:
                    for i in range(x + 1, x1):
                        y = y + 1
                        position = i, y
                        if self.isValidateMoveToRangeOfPosition(position, "b") == True:
                            return False
                elif x > x1 and y < y1:
                    for i in range(x1 + 1, x):
                        y = y + 1
                        position = i, y
                        if self.isValidateMoveToRangeOfPosition(position, "b") == True:
                            return False
                elif x < x1 and y > y1:
                    for i in range(x + 1, x1):
                        y1 = y1 + 1
                        position = i, y1
                        if self.isValidateMoveToRangeOfPosition(position, "b") == True:
                            return False
            return True

    def isValidateEscapeToKing(self, king, kingPosition, colorKing):
        for i in range(-1,2):
            for j in range(-1,2):
                if i != 0 and j != 0:
                    if king.isValidateMove(kingPosition, (kingPosition[0] + i, kingPosition[1]+j)) == True:
                        king.currentPosition = kingPosition[0] + i, kingPosition[1]+j
                        if self.isKingUnderAttack(colorKing) == False:
                            king.currentPosition = kingPosition[0] - i, kingPosition[1] - j
                            return True
                        king.currentPosition = kingPosition[0] - i, kingPosition[1] - j
        return False

    def pawnPromotion(self, position, piece):
        if self.getColorFromBoard(position) == "w" and piece.currentPosition[0] == 1:
            x,y = position
            x = x-1
            position = x, y
            self.removeFromWhiteList(piece)
            piece.removePiece(piece.currentPosition)
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
        elif self.colorAi == "b" and piece.currentPosition[0] == 6:
            x, y = position
            x = x + 1
            position = x, y
            self.removing(piece)
            piece.removePiece(piece.currentPosition)  #
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
        queen = Queen(position,color,self.chessboard)
        self.placePiece(queen,position)
        self.whitePlayer.addFigury(queen)
        return queen






