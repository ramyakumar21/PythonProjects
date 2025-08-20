import turtle
from turtle import Turtle
PADDLE_LEN = 1
PADDLE_WIDTH = 5
MOVING_DIST = 20


class Paddle(Turtle):

    def __init__(self, coord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)
        self.goto(coord)

    def up(self):
        new_y = self.ycor() + MOVING_DIST
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVING_DIST
        self.goto(self.xcor(), new_y)




