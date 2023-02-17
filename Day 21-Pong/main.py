from turtle import Screen
from paddle import Paddle
from ball import Ball
from background import Background
from scoreboard import  Scoreboard
import time

screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("#323031")
screen.listen()

# Initialize background
background = Background()
background.draw_half_way_line()

# Initialize scoreboard
scoreboard = Scoreboard()
scoreboard.score()


# Initiate paddle
left_paddle = Paddle("left")
right_paddle = Paddle("right")

# paddle control
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

# Initiate ball
ball = Ball()

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 80 and ball.xcor() > 300:
        ball.bounce_x()
        ball.speed_up()

    if ball.distance(left_paddle) < 80 and ball.xcor() < -300:
        ball.bounce_x()
        ball.speed_up()

    if ball.xcor() > 320:
        time.sleep(0.1)
        scoreboard.upgrade_score("right")
        ball.reset_position()


    if ball.xcor() < -320:
        time.sleep(0.1)
        scoreboard.upgrade_score("left")
        ball.reset_position()


screen.exitonclick()

