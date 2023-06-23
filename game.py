from board import *
from cell import *
import random
class Game(Board):
    def __init__(self):
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
                        print("nie mozesz narazac krola")
                        return False
                    elif self.getCellFromBoard(end).getPiece().type == "bp":
                        self.getCellFromBoard(end).piece.move_base(start)
                        print("nie mozesz narazac krola")
                        return False
                    else:
                        self.getCellFromBoard(end).piece.move(end, start)
                        print("nie mozesz narazac krola")
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
            if self.getPieceFromBoard((start)) == "wp" or "bp":
                if self.pawnPromotion(start, self.getPieceFromBoard(start)) == True:
                    return True
            myColor = self.getColorFromBoard(start)
            move = self.getCellFromBoard(start).piece.move(start, end)
            if self.isKingUnderAttack(myColor) == True:
                if self.getCellFromBoard(end).getPiece().type == "wp":
                    self.getCellFromBoard(end).piece.move_base(start)
                    print("nie mozesz narazac krola")
                    return False
                elif self.getCellFromBoard(end).getPiece().type == "bp":
                    self.getCellFromBoard(end).piece.move_base(start)
                    print("nie mozesz narazac krola")
                    return False
                else:
                    self.getCellFromBoard(end).piece.move(end, start)
                    print("nie mozesz narazac krola")
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
        if color == "w":
            kingPosition = self.k2.currentPosition
            opponentPieces = self.blackPlayer.figury
        else:
            kingPosition = self.k1.currentPosition
            opponentPieces = self.whitePlayer.figury

        for i in range(len(opponentPieces)):
            if opponentPieces[i] is not None:
                self.currentPiece = opponentPieces[i]
                if self.currentPiece.isValidateMove(self.currentPiece.currentPosition, kingPosition) == "kill":
                    self.attackerPosition = self.currentPiece.currentPosition
                    self.attacker = self.currentPiece
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
            self.king = self.k2
            self.kingPosition = self.k2.currentPosition
            self.myPieces = whitePieces
        else:
            self.king = self.k1
            self.kingPosition = self.k1.currentPosition
            self.myPieces = blackPieces

        for i in range(len(self.myPieces)):
            if self.myPieces[i] is not None:
                self.myPiece = self.myPieces[i]
                if self.myPiece.isValidateMove(self.myPiece.currentPosition, self.attackerPosition) == "kill":
                    if self.isKingUnderAttack(kingColor) == False:
                        return False

        if self.isValidateEscapeToKing(self.king, self.king.currentPosition, self.king.color) == True:
            if self.isKingUnderAttack(kingColor) == False:
                return False
        #spr czy na ta pozycje moze pojsc jakas nasza figura
        if self.attacker.type != "bn" and self.attacker.type != "wn":
            x, y = self.kingPosition
            x1, y1 = self.attackerPosition
            dx = x - x1
            dy = y - y1

            if dx == 0:
                start, end = (y1 + 1, y) if dy > 0 else (y, y1 - 1)
                for i in range(start, end):
                    position = x, i
                    if self.isValidateMoveToRangeOfPosition(position, kingColor) == True:
                        if self.isKingUnderAttack(kingColor) == False:
                            return False
            elif dy == 0:
                start, end = (x1 + 1, x) if dx > 0 else (x, x1 - 1)
                for i in range(start, end):
                    position = i, y
                    if self.isValidateMoveToRangeOfPosition(position, kingColor) == True:
                        if self.isKingUnderAttack(kingColor) == False:
                            return False
            else:
                start_x, end_x = (x1 + 1, x) if dx > 0 else (x, x1 - 1)
                start_y, end_y = (y1 + 1, y) if dy > 0 else (y, y1 - 1)

                for i, j in zip(range(start_x, end_x), range(start_y, end_y)):
                    position = i, j
                    if self.isValidateMoveToRangeOfPosition(position, kingColor) == True:
                        if self.isKingUnderAttack(kingColor) == False:
                            return False
        return True

    def isValidateEscapeToKing(self, king, kingPosition, colorKing):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 and j != 0:
                    if king.isValidateMove(kingPosition, (kingPosition[0] + i, kingPosition[1]+j)) == True:
                        king.currentPosition = kingPosition[0] + i, kingPosition[1]+j
                        if self.isKingUnderAttack(colorKing) == False:
                            king.currentPosition = kingPosition[0] - i, kingPosition[1] - j
                            return True
                        king.currentPosition = kingPosition[0] - i, kingPosition[1] - j
        return False

    def pawnPromotion(self, position, piece):
        if self.getColorFromBoard(position) == "w" and piece.currentPosition[0] == 1 or self.getColorFromBoard(position) == "b" and piece.currentPosition[0] == 6:
            if piece.color == "w":
                x, y = position
                x = x - 1
                position = x, y
                self.removeFromWhiteList(piece)
                piece.removePiece(piece.currentPosition)
            else:
                x, y = position
                x = x + 1
                position = x, y
                self.removing(piece)
                piece.removePiece(piece.currentPosition)

            for i in range(3, 15):
                if not hasattr(self, f'q{i}'):
                    q = None
                    self.creatingNewQueen(q, position, piece.color)
                    setattr(self, f'q{i}', q)
                    return True
        return False

    def creatingNewQueen(self, queen, position,color):
        self.removePiece(position)
        self.queen = queen
        queen = Queen(position,color,self.chessboard)
        self.placePiece(queen,position)
        self.whitePlayer.addFigury(queen)
        return queen






