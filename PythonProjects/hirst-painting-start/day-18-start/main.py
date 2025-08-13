import turtle
import random

def random_colour():

    red = random.choice(range(0, 256))
    green = random.choice(range(0, 256))
    blue = random.choice(range(0, 256))
    return tuple([red, green, blue])

jimmy = turtle.Turtle()
# jimmy.shape("turtle")
# jimmy.color("#FF69B4")

# 1. Draw a square

# for x in range(0, 4):
#     jimmy.forward(100)
#     jimmy.right(90)

# 2. Draw a dashed line

# for x in range(15):
#     jimmy.forward(10)
#     jimmy.penup()
#     jimmy.forward(10)
#     jimmy.pendown()

# 3. Draw polygons

# def print_polygon(sides):
#     angle = 360 / sides
#     for y in range(sides):
#         jimmy.forward(100)
#         jimmy.right(angle)
#
#
#
# for num in range (3, 11):
#     red = random.choice(range(0, 256))
#     green = random.choice(range(0, 256))
#     blue = random.choice(range(0, 256))
#     turtle.colormode(255)
#     jimmy.pencolor(red, green, blue)
#     print_polygon(num)




#  4. Random Walk
# angles = [0, 90, 180, 270]
# jimmy.speed(10)
# jimmy.width(15)
#
# for x in range(50):
#     turtle.colormode(255)
#     jimmy.pencolor(random_colour())
#     jimmy.forward(25)
#     jimmy.right(random.choice(angles))
#

# 5. Draw Spirograph

jimmy.speed(0)

for x in range(0, 361, 10):
    turtle.colormode(255)
    turtle.pencolor(random_colour())
    turtle.setheading(x)
    turtle.circle(100)




screen = turtle.Screen()
#screen.screensize(2500, 300)
screen.exitonclick()