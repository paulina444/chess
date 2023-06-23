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

    def move(self, start, end):
        self.start = self.currentPosition
        self.end = end
        isvalidate = self.isValidateMove(start,end)
        if isvalidate == True:
            self.move_base(self.end)
            return True
        elif isvalidate == "kill":
            self.removePiece(self.end)
            self.move_base(self.end)
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
        if self.isOutOfBoard(end) == True:
            return False
        elif self.isOccupiedPosition(end) == False:
            if self.getColorFromBoard((x,y)) != self.getColorFromBoard((x1,y1)):
                return "kill"
            else:
                return False
        else:
            return True

    def isEmptyVerticalAndChorizontal(self, currentPosition, newPosition):
        x1, y1 = currentPosition
        x2, y2 = newPosition
        if x1 == x2:
            direction = 1 if y2 > y1 else -1
            for i in range(y1 + direction, y2, direction):
                position = x1, i
                if self.isOccupiedPosition(position) == False:
                    return False
        elif y1 == y2:
            direction = 1 if x2 > x1 else -1
            for i in range(x1 + direction, x2, direction):
                position = i, y1
                if self.isOccupiedPosition(position) == False:
                    return False
        return True

    def isEmptyDiagonal(self, currentPosition, newPosition):
        x1, y1 = currentPosition
        x2, y2 = newPosition
        length_x = abs(x1 - x2)
        length_y = abs(y1 - y2)
        if x1 != x2 and y1 != y2:
            if length_x != length_y:
                return False

            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            x = x1 + dx
            y = y1 + dy

            while (x != x2) and (y != y2):
                position = x, y
                if self.isOutOfBoard(position) == True or self.isOccupiedPosition(position) == False:
                    return False
                x += dx
                y += dy
        return True

    def checkKills(self, currentPosition):
        pass

    def checkKillsChorizontalandVertical(self, currentPosition):
        x1, y1 = currentPosition
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            dx, dy = direction
            i = 1
            while True:
                position = x1 + i * dx, y1 + i * dy
                if self.isOutOfBoard(position) == True:
                    break
                if self.isOccupiedPosition(position) == False:
                    if self.move(currentPosition, position) == "kill":
                        return True
                    break
                i += 1
        return False

    def checkKillsDiagonal(self, currentPosition):
        x1, y1 = currentPosition
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for direction in directions:
            dx, dy = direction
            for i in range(1, 8):
                position = x1 + i * dx, y1 + i * dy
                if self.isOutOfBoard(position) == True:
                    break
                if self.isOccupiedPosition(position) == False:
                    if self.move(currentPosition, position) == "kill":
                        return True
                    break
        return False

    def checkKillsOneField(self, currentPosition):
        x1, y1 = currentPosition
        moves = [(1, 0), (1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (-1, 1), (1, -1)]

        for move in moves:
            position = x1 + move[0], y1 + move[1]
            if self.ifOutOfBoardAndIsValidPositionAndKill(position, currentPosition) == True:
                return True
        return False

    def checkKillsOneFieldDiagonal(self, currentPosition):
        x1, y1 = currentPosition
        color = self.getColorFromBoard(currentPosition)
        if color == "w":
            diagonal_moves = [(-1, 1), (-1, -1)]
        else:
            diagonal_moves = [(1, -1), (1, 1)]
        for move in diagonal_moves:
            position = x1 + move[0], y1 + move[1]
            if self.ifOutOfBoardAndIsValidPositionAndKill(position, currentPosition) == True:
                return True
        return False

    def checkKillsKnight(self, currentPosition):
        x1, y1 = currentPosition
        knight_moves = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, -2), (-1, -2), (-1, 2), (1, 2)]
        for move in knight_moves:
            position = x1 + move[0], y1 + move[1]
            if self.ifOutOfBoardAndIsValidPositionAndKill(position, currentPosition) == True:
                return True
        return False

    def ifOutOfBoardAndIsValidPositionAndKill(self, position, currentPosition):
        if self.isOutOfBoard(position) == True:
            return False
        else:
            if self.isOccupiedPosition(position) == False:
                move = self.move(currentPosition, position)
                if move == "kill":
                    return True
                else:
                    return False
            else:
                return False

    def isOutOfBoard(self, position):
        x, y = position
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            return True
        else:
            return False

    def isOccupiedPosition(self,position):
        x, y = position
        chessboard = self.board
        if self.isOutOfBoard(position) == False:
            cell = chessboard[x][y]
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