from board import *
import random
class Piece:
    def __init__(self, currentPosition, type, board):
        self.currentPosition = currentPosition
        self.type = type
        self.board = board

    def getPiece(self):
        return self.currentPosition, self.type

    def setPiece(self, newCurrentPosition, newType):
        self.currentPosition = newCurrentPosition
        self.type = newType
        return self.currentPosition, self.type

    def move_base(self, destination):
        current_position = self.currentPosition
        self.removePiece(current_position)
        self.currentPosition = destination
        self.placePiece(self, destination)

    def move(self, skad, new_position):
        self.skad = self.currentPosition
        self.new_position = new_position
        isvalidate = self.isValidateMove(skad,new_position)
        if isvalidate == True:
            self.move_base(self.new_position)
            return True
        elif isvalidate == "kill":
            self.removePiece(self.new_position)
            self.move_base(self.new_position)
            return "kill"
        else:
            return False

    def getCellFromBoard(self, position):
        x, y = position
        return self.board[x][y]

    def getColorFromBoard(self, position):
        x, y = position
        if self.getCellFromBoard((x, y)).getPiece() is None:
            return False
        return self.getCellFromBoard((x, y)).getPiece().color

    def getPieceFromBoard(self, position):
        x, y = position
        return self.getCellFromBoard((x, y)).getPiece()

    def isValidateMove(self, start, end):
        self.end = end
        x,y = end
        x1, y1 = start
        if self.isOutOfBoard(end) == False:
            return False
        elif self.isOccupiedPosition(end) == False:
            if self.getColorFromBoard((x,y)) != self.getColorFromBoard((x1,y1)):
                return "kill"
            else:
                return False
        else:
            return True

    def isEmptyDiagonal(self, currentPosition, new_position):
        x, y = new_position
        x1, y1 = currentPosition
        length_x = abs(x1 - x)
        length_y = abs(y1 - y)

        if x1 > x and y1 < y:
            if length_y != length_x:
                return False
            for i in range(x1 - length_x + 1, x1):
                position = i, y - 1
                y = y - 1
                if self.isOutOfBoard(position) == True:
                    if self.isOccupiedPosition(position) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        elif x1 > x and y1 > y:
            if length_y != length_x:
                return False
            y1 = y1 - length_x
            for i in range(x1 - length_x + 1, x1):
                position = i, y1 + 1
                y1 = y1 + 1
                if self.isOutOfBoard(position) == True:
                    if self.isOccupiedPosition(position) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        elif x1 < x and y1 > y:
            if length_y != length_x:
                return False
            for i in range(x1 + 1, x):
                y1 = y1 - 1
                position = i, y1
                if self.isOutOfBoard(position) == True:
                    if self.isOccupiedPosition(position) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        elif x1 < x and y1 < y:
            if length_y != length_x:
                return False
            for i in range(x1 + 1, x):
                y1 = y1 + 1
                position = i, y1
                if self.isOutOfBoard(position) == True:
                    if self.isOccupiedPosition(position) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        return True

    def isEmptyVertical(self, currentPosition, new_position):
        x, y = new_position
        x1, y1 = currentPosition
        how_many = abs(x1 - x)
        if x1 < x:
            for i in range(x1 + 1, x1 + how_many):
                position = i, y
                if self.isOutOfBoard(position) == True:
                    if self.isOccupiedPosition(position) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        else:
            for i in range(x1+ 1 - how_many, x1):
                position = i, y
                if self.isOutOfBoard(position) == True:
                    if self.isOccupiedPosition(position) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        return True

    def isEmptyHorizontal(self, currentPosition, new_position):
        x, y = new_position
        x1, y1 = currentPosition
        how_many = abs(y1 - y)
        if y1 < y:
            for i in range(y1 + 1, y1 + how_many):
                position = x, i
                if self.isOutOfBoard(position) == True:
                    if self.isOccupiedPosition(position) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        else:
            for i in range(y1 - how_many + 1, y1):
                position = x, i
                if self.isOutOfBoard(position) == True:
                    if self.isOccupiedPosition(position) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        return True

    def checkKills(self, currentPosition):
        pass

    def checkKillsVertical(self, currentPosition):
        x1, y1 = currentPosition
        for i in range(1, 8):
            position = x1+i, y1
            if self.isOutOfBoard(position) == False:
                break
            if self.isOccupiedPosition(position) == False:
                if self.move(currentPosition, position) == "kill":
                    return True
                else:
                    break
        for i in range(1, 8):
            position = x1-i, y1
            if self.isOutOfBoard(position) == False:
                break
            if self.isOccupiedPosition(position) == False:
                if self.move(currentPosition, position) == "kill":
                    return True
                else:
                    break
        return False

    def checkKillsChorizontal(self, currentPosition):
        x1, y1 = currentPosition
        for i in range(1, 8):
            position = x1, y1 + i
            if self.isOutOfBoard(position) == False:
                break
            if self.isOccupiedPosition(position) == False:
                if self.move(currentPosition, position) == "kill":
                    return True
                else:
                    break
        for i in range(1, 8):
            position = x1, y1 - i
            if self.isOutOfBoard(position) == False:
                break
            if self.isOccupiedPosition(position) == False:
                if self.move(currentPosition, position) == "kill":
                    return True
                else:
                    break
        return False

    def checkKillsDiagonal(self, currentPosition):
        x1, y1 = currentPosition
        for i in range(1, 8):
            position = x1+i, y1+i
            if self.isOutOfBoard(position) == False:
                break
            if self.isOccupiedPosition(position) == False:
                if self.move(currentPosition, position) == "kill":
                    return True
                else:
                    break

        for i in range(1, 8):
            position = x1+i, y1-i
            if self.isOutOfBoard(position) == False:
                break
            if self.isOccupiedPosition(position) == False:
                if self.move(currentPosition, position) == "kill":
                    return True
                else:
                    break

        for i in range(1, 8):
            position = x1-i, y1+i
            if self.isOutOfBoard(position) == False:
                break
            if self.isOccupiedPosition(position) == False:
                if self.move(currentPosition, position) == "kill":
                    return True
                else:
                    break

        for i in range(1, 8):
            position = x1-i, y1-i
            if self.isOutOfBoard(position) == False:
                break
            if self.isOccupiedPosition(position) == False:
                if self.move(currentPosition, position) == "kill":
                    return True
                else:
                    break
        return False

    def checkKillsOneField(self, currentPosition):
        x1, y1 = currentPosition
        position = x1 + 1, y1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 + 1, y1 + 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 - 1, y1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 - 1, y1 - 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1, y1 + 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1, y1 - 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 - 1, y1 + 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 + 1, y1 - 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        return False

    def checkKillsOneFieldDiagonal(self, currentPosition):
        x1, y1 = currentPosition
        if self.getColorFromBoard(currentPosition) == "w":
            position = x1 - 1, y1 + 1
            if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
                return True
            position = x1 - 1, y1 - 1
            if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
                return True
            return False
        else:
            position = x1 + 1, y1 - 1
            if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
                return True
            position = x1 + 1, y1 + 1
            if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
                return True
            return False

    def checkKillsKnight(self, currentPosition):
        x1, y1 = currentPosition
        position = x1 + 2, y1 - 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 + 2, y1 + 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 - 2, y1 + 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 - 2, y1 - 1
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 + 1, y1 - 2
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 - 1, y1 - 2
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 - 1, y1 + 2
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        position = x1 + 1, y1 + 2
        if self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition) == True:
            return True
        return False

    def ifOutOfBoardAndIsValidPositionAndMove(self, position, currentPosition):
        if self.isOutOfBoard(position) == False:
            return False
        else:
            if self.isOccupiedPosition(position) == False:
                move = self.move(currentPosition, position)
                if move == True or move == "kill":
                    return True
                else:
                    return False
            else:
                return False

    def isOutOfBoard(self, position):
        x, y = position
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            return False
        else:
            return True

    def isOccupiedPosition(self,position):
        x, y = position
        chessboard = self.board
        cell = chessboard[x][y]
        if self.isOutOfBoard(position)==True:
            if cell.piece is None:
                return True
            else:
                return False
        else:
            return False

    def placePiece(self, piece, position):
        x, y = position
        self.board[x][y].setCell(x, y, piece)

    def removePiece(self, position):
        x, y = position
        self.board[x][y].setCell(x, y, None)