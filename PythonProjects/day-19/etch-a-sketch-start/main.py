from turtle import Turtle, Screen

jimmy = Turtle()
screen = Screen()


def move_forwards():
    jimmy.forward(10)

def move_backwards():
    jimmy.back(10)

def turn_left():
    jimmy.left(10)

def turn_right():
    jimmy.right(10)

def clear_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
