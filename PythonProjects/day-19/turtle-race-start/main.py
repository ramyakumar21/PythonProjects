from turtle import Turtle, Screen
import random

colours_list = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

screen = Screen()
screen.setup(width= 500, height= 400)
user_choice = screen.textinput(title="Welcome to the turtle race! Make a bet", prompt="Choose your turtle: violet, indigo, blue, green, yellow, orange, red")

turtle_list = []
x_coord = -230
y_coord = -140
is_race_on = False

for incr in range(0, 7):
    jimmy = Turtle(shape="turtle")
    jimmy.penup()
    jimmy.color(colours_list[incr])
    jimmy.setpos(x=x_coord, y=y_coord)
    turtle_list.append(jimmy)
    y_coord += 40

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 220:
            is_race_on = False
            if user_choice == turtle.pencolor():
                print(f"You've won! {turtle.pencolor()} is the winning colour.")
            else:
                print(f"You've lost! {turtle.pencolor()} is the winning colour.")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()