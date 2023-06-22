from ai import *
class Main(Ai):
    def play(self):
        myColor = input("podaj jakim kolorem chcesz byc (w=white, b=black)")
        if myColor == "b":
            self.colorAi = "w"
        else:
            self.colorAi = "b"

        if self.colorAi == "w":
            self.moveAi()
        while True:
            self.displayBoard()
            print("Graczu, podaj, gdzie chcesz się ruszyć (w formacie a5-a6):")
            move = input()
            start, end = move.split('-')
            x = self.convertToBoard(start)
            y = self.convertToBoard(end)

            if self.move(x, y) == False:
                while True:
                    print("zly move musisz podac jeszcze raz")
                    move = input()
                    start, end = move.split('-')
                    x = self.convertToBoard(start)
                    y = self.convertToBoard(end)
                    move = self.move(x, y)
                    if move == True or move == "kill":
                        break
            self.moveAi()

game1 = Main()
game1.creatingNewBoard()
game1.play()