from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)

    def display(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="center", font= FONT)

    def level_up(self):
        self.level += 1
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font= FONT)


