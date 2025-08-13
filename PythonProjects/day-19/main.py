# higher order functions and event listeners

import turtle

jimmy = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    return jimmy.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()