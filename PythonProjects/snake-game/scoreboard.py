from turtle import Turtle

ALIGN = "Center"
FONT = ('Courier', 12, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.penup()
        self.color("white")
        self.update_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", move=False, align=ALIGN, font=FONT)

