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
        self.remove_piece(current_position)  # Usunięcie pionka z poprzedniej pozycji
        self.currentPosition = destination  # Ustawienie nowej pozycji pionka
        self.place_piece(self, destination)  # Wstawienie pionka na nową pozycję

    def move(self, skad, new_position):
        pass

    def moveAi(self):
        pass
    def getCellFromBoard(self, position):
        x, y = position
        return self.board[x][y]

    def getColorFromBoard(self, position):
        x, y = position
        if self.getCellFromBoard((x,y)).getPiece() is None:
            print("None nie ma tam pionka")
            return False
        return self.getCellFromBoard((x,y)).getPiece().color

    def getPieceFromBoard(self, position):
        x, y = position
        return self.getCellFromBoard((x, y)).getPiece()

    def isValidateMove(self, destination, skad):
        szachownica = self.board
        self.destination = destination
        x,y = destination
        x1, y1 = skad
        if self.is_valid_position(destination) == False: #ruch poza plansza
            return False
        elif self.is_occupied_position(destination) == False: #tutaj jest szachowanie
            if self.getColorFromBoard((x,y)) != self.getColorFromBoard((x1,y1)):
                self.remove_piece((x,y))
            else: #Nieprawidłowy ruch - docelowa pozycja zajęta przez twoja figure
                return False
        else:
            return True

    def isEmptySkosy(self, currentPosition, new_position):
        x, y = new_position
        x1, y1 = currentPosition
        length_x = abs(x1 - x)
        length_y = abs(y1 - y)

        if x1==x or y1==y:
            return False
        elif x1 > x and y1 < y:  # od dolu na pawo
            if length_y != length_x:
                return False
            for i in range(x1 - length_x + 1, x1):
                pozycja = i, y - 1
                y = y - 1
                if self.is_valid_position(pozycja) == True:
                    if self.is_occupied_position(pozycja) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        elif x1 > x and y1 > y:  # od dolu na lewo
            if length_y != length_x:
                return False
            y1 = y1 - length_x
            for i in range(x1 - length_x + 1, x1):
                pozycja = i, y1 + 1
                y1 = y1 + 1
                if self.is_valid_position(pozycja) == True:
                    if self.is_occupied_position(pozycja) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        elif x1 < x and y1 > y:  # skos od gory do dolu lewy
            if length_y != length_x: # gdy nie jest to ruch po przekatnej
                return False
            for i in range(x1 + 1, x):
                y1 = y1 - 1
                pozycja = i, y1
                if self.is_valid_position(pozycja) == True:
                    if self.is_occupied_position(pozycja) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        elif x1 < x and y1 < y:  # skos do dolu w prawo
            if length_y != length_x:
                return False
            for i in range(x1 + 1, x):
                y1 = y1 + 1
                pozycja = i, y1
                if self.is_valid_position(pozycja) == True:
                    if self.is_occupied_position(pozycja) == True:
                        continue
                    else:
                        return False
                else:
                    return False
        return True

    def isEmptyVertical(self, currentPosition, new_position):  # czy nie pionkow w pionieprzeskakuje w pionie
        x, y = new_position
        x1, y1 = currentPosition
        how_many = abs(x1 - x)
        # jesli czarny
        if x1 < x:
            for i in range(x1 + 1, x1 + how_many):
                pozycja = i, y
                if self.is_valid_position(pozycja) == True:
                    if self.is_occupied_position(pozycja) == True:
                        continue  # pusta
                    else:
                        return False
                else:
                    return False
        else:
            for i in range(x1+ 1 - how_many, x1):
                pozycja = i, y
                if self.is_valid_position(pozycja) == True:
                    if self.is_occupied_position(pozycja) == True:
                        continue  # pusta
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
                pozycja = x, i
                if self.is_valid_position(pozycja) == True:
                    if self.is_occupied_position(pozycja) == True:
                        continue  # pusta
                    else:
                        return False
                else:
                    return False
        else:
            for i in range(y1 - how_many + 1, y1):
                pozycja = x, i
                if self.is_valid_position(pozycja) == True:
                    if self.is_occupied_position(pozycja) == True:
                        continue  # pusta
                    else:
                        return False
                else:
                    return False
        return True

    def checkKillsVertical(self, currentPosition):
        x1, y1 = currentPosition
        # Sprawdź 7 pozycje do gory
        for i in range(1, 8):
            position = x1+i, y1
            if self.is_valid_position(position) == False: #jesli  wychodzi poza plansze
                break
            if self.is_occupied_position(position) == False:#jesli jest okupowana
                a=self.getPieceFromBoard(position)
                if self.move(currentPosition, position) == True:
                    return a
                else:
                    break
        #w dol
        for i in range(1, 8):
            position = x1-i, y1
            if self.is_valid_position(position) == False: #jesli wychodzi poza plansze
                break
            if self.is_occupied_position(position) == False:#jesli jest okupowana
                a = self.getPieceFromBoard(position)
                if self.move(currentPosition, position) == True:
                    return a
                else:
                    break
        return False #-nie ma killow

    def checkKillsChorizontal(self, currentPosition):
        x1, y1 = currentPosition
        # Sprawdź 7 pozycje w prawo
        for i in range(1, 8):
            position = x1, y1 + i
            if self.is_valid_position(position) == False:  # jesli  wychodzi poza plansze
                break
            if self.is_occupied_position(position) == False:  # jesli jest okupowana
                a = self.getPieceFromBoard(position)
                if self.move(currentPosition, position) == True:
                    return a  # no bo zabilo
                else:
                    break
        # w lewo
        for i in range(1, 8):
            position = x1, y1 - i
            if self.is_valid_position(position) == False:  # jesli wychodzi poza plansze
                break
            if self.is_occupied_position(position) == False:  # jesli jest okupowana
                a = self.getPieceFromBoard(position)
                if self.move(currentPosition, position) == True:
                    return a
                else:
                    break
        return False  # -nie ma killow

    def checkKillsSkosy(self, currentPosition):
        x1, y1 = currentPosition
        #trzeba kazdy skos sprawdzic
        for i in range(1, 8): #skos od lewy gora do prawy dol
            position = x1+i, y1+i
            if self.is_valid_position(position) == False:  # jesli wychodzi poza plansz
                break
            if self.is_occupied_position(position) == False:  # jesli jest okupowana
                a = self.getPieceFromBoard(position)
                if self.move(currentPosition, position) == True:
                    return a
                else:
                    break

        for i in range(1, 8): #skos prawy goa do lewy dol
            position = x1+i, y1-i
            if self.is_valid_position(position) == False:  # jesli wychodzi poza plansz
                break
            if self.is_occupied_position(position) == False:  # jesli jest okupowana
                a = self.getPieceFromBoard(position)
                if self.move(currentPosition, position) == True:
                    return a
                else:
                    break
        for i in range(1, 8): #skos lewy dol do prawy gora
            position = x1-i, y1+i
            if self.is_valid_position(position) == False:  # jesli wychodzi poza plansz
                break
            if self.is_occupied_position(position) == False:  # jesli jest okupowana
                a = self.getPieceFromBoard(position)
                if self.move(currentPosition, position) == True:
                    return a
                else:
                    break

        for i in range(1, 8): #skos prawy dol do lewa gora
            position = x1-i, y1-i
            if self.is_valid_position(position) == False:  # jesli wychodzi poza plansz
                break
            if self.is_occupied_position(position) == False:  # jesli jest okupowana
                a = self.getPieceFromBoard(position)
                if self.move(currentPosition, position) == True:
                    return a
                else:
                    break

        return False

    def checkKillsOneField(self, currentPosition):
        x1, y1 = currentPosition
        position = x1+1, y1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete

        position = x1 + 1, y1 + 1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete

        position = x1 -1, y1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete

        position = x1-1, y1-1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete

        position = x1, y1 + 1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete

        position = x1, y1 - 1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete

        position = x1 - 1, y1 + 1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete

        position = x1 + 1, y1 - 1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete

        return False

    def checkKillsOneFieldSkosy(self, currentPosition):
        x1, y1 = currentPosition
        if self.getColorFromBoard(currentPosition) == "w":
            position = x1-1, y1+1
            pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
            if pieceToDelete != False:
                return pieceToDelete
            position = x1 - 1, y1-1
            pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
            if pieceToDelete != False:
                return pieceToDelete
            return False
        else:
            position = x1+1, y1-1
            pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
            if pieceToDelete != False:
                return pieceToDelete
            position = x1+1, y1+1
            pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
            if pieceToDelete != False:
                return pieceToDelete
            return False

    def checkKillsKnight(self, currentPosition):
        x1, y1 = currentPosition
        position = x1+2, y1-1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete
        position = x1+2, y1+1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete
        position = x1-2, y1+1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete
        position = x1-2, y1-1
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete
        position = x1+1, y1-2
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete
        position = x1-1, y1-2
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete
        position = x1-1, y1+2
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete
        position =x1+1, y1+2
        pieceToDelete = self.ifOutOfBoardAndIsValidPositionAndMove(position, currentPosition)
        if pieceToDelete != False:
            return pieceToDelete
        return False

    def ifOutOfBoardAndIsValidPositionAndMove(self, position, currentPosition):
        if self.is_valid_position(position) == False:  # jesli  wychodzi poza plansze
            return False
        else:
            if self.is_occupied_position(position) == False:  # jesli jest okupowana czyli moze uda sie zabic jesli jest to przeciwnik
                a = self.getPieceFromBoard(position)
                if self.move(currentPosition, position) == True:
                    return a
                else:
                    return False
            else:
                return False

    # sprawdza czy nie wychodzi poza plansze
    def is_valid_position(self, position):
        x, y = position
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            return False
        else:
            return True

    def is_occupied_position(self,position):
        x, y = position
        szachownica = self.board
        cell = szachownica[x][y]
        if self.is_valid_position(position)==True:
            if cell.piece is None:
                return True
            else:
                return False
        else:
            return False

    def place_piece(self, piece, position):
        x, y = position
        szachownica = self.board
        self.board[x][y].setCell(x, y, piece)

    def remove_piece(self, position):
        x, y = position
        self.board[x][y].setCell(x, y, None)












