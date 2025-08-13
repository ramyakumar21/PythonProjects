
import colorgram
import turtle
import random


# Extract colours from image
# rgb_image = []
# colour = colorgram.extract('image.jpg', 30)
# for x in colour:
#     new_colour = (x.rgb.r, x.rgb.g, x.rgb.b)
#     rgb_image.append(new_colour)
#
# print(rgb_image)

colours_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
jimmy = turtle.Turtle()
screen = turtle.Screen()

jimmy.penup()
jimmy.hideturtle()

def random_colour():
    colour = random.choice(colours_list)
    return colour

def draw_dot(x_coord, y_coord):
    jimmy.setpos(-360 + x_coord, -360 + y_coord)
    turtle.colormode(255)
    jimmy.dot(20, random_colour())
    jimmy.forward(50)


for y in range(0, 500, 50):
    for x in range(0, 500, 50):
        draw_dot(x, y)








screen.exitonclick()

