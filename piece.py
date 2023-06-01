from board import *
class Piece():
    def __init__(self, currentPosition, type, board):
        self.currentPosition = currentPosition
        self.type = type
        self.board = board

    def getColor(self):
        return self.getColor()

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

    def getCellFromBoard(self, position):
        x, y = position
        return self.board[x][y]

    def getColorFromBoard(self, position):
        x, y = position
        return self.getCellFromBoard((x,y)).getPiece().color

    def getPieceFromBoard(self, position):
        x, y = position
        return self.getCellFromBoard((x, y)).getPiece()

    def isValidateMove(self, destination, skad):
        szachownica = self.board
        self.destination = destination
        x,y = destination
        x1, y1 = skad
        if self.is_valid_position(destination) == False:
            print("Nieprawidłowy ruch - poza planszą.")
            return False
        elif self.is_occupied_position(destination) == False:
            if self.getColorFromBoard((x,y)) != self.getColorFromBoard((x1,y1)):
                self.remove_piece((x,y))
            else:
                print("Nieprawidłowy ruch - docelowa pozycja zajęta przez twoja figure")
                return False





    def isEmptySkosy(self, currentPosition, new_position):
        x, y = new_position
        x1, y1 = currentPosition
        length_x = abs(x1 - x)
        length_y = abs(y1 - y)

        if x1 > x and y1 < y:  # od dolu na pawo
            if length_y != length_x:
                print("nie jest ruch po przekątnej")
                return False
            for i in range(x1 - length_x + 1, x1):
                pozycja = i, y - 1
                y = y - 1
                if self.is_occupied_position(pozycja) == True:
                    continue
                else:
                    return False
        elif x1 > x and y1 > y:  # od dolu na lewo
            if length_y != length_x:
                print("nie jest ruch po przekątnej")
                return False
            y1 = y1 - length_x
            for i in range(x1 - length_x + 1, x1):
                pozycja = i, y1 + 1
                y1 = y1 + 1
                if self.is_occupied_position(pozycja) == True:
                    continue
                else:
                    return False
        elif x1 < x and y1 > y:  # skos od gory do dolu lewy
            if length_y != length_x:
                print("nie jest ruch po przekątnej")
                return False
            for i in range(x1 + 1, x):
                y1 = y1 - 1
                pozycja = i, y1
                if self.is_occupied_position(pozycja) == True:
                    continue
                else:
                    return False
        elif x1 < x and y1 < y:  # skos do dolu w prawo
            if length_y != length_x:
                print("nie jest ruch po przekątnej")
                return False
            for i in range(x1 + 1, x):
                y1 = y1 + 1
                pozycja = i, y1
                if self.is_occupied_position(pozycja) == True:
                    continue
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
                if self.is_occupied_position(pozycja) == True:
                    continue  # pusta
                else:
                    return False
        else:
            for i in range(x1 - how_many, x1):
                pozycja = i, y
                if self.is_occupied_position(pozycja) == True:
                    continue  # pusta
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
                if self.is_occupied_position(pozycja) == True:
                    continue  # pusta
                else:
                    return False
        else:
            for i in range(y1 - how_many + 1, y1):
                pozycja = x, i
                if self.is_occupied_position(pozycja) == True:
                    continue  # pusta
                else:
                    return False
        return True

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
        if cell.piece is None:
            return True
        else:
            return False

    def place_piece(self, piece, position): #ustawia pionki
        x, y = position
        szachownica = self.board
        self.board[x][y].setCell(x, y, piece)

    def remove_piece(self, position):
        x, y = position
        self.board[x][y].setCell(x, y, None)




