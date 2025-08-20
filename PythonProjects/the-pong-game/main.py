import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    #Detect collision with top and bottom walls

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    #Detect collision with paddle

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when ball goes out of bounds for right paddle

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect when ball goes out of bounds for left paddle

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()