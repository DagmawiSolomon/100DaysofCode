from turtle import Turtle
from background import Background


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#FFFFFF")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.x_move = 10
        self.y_move = 10
        self.goto(0, 0)
        self.bounce_x()

    def speed_up(self):
        self.x_move *= 1.5
        self.y_move *= 1.5
        self.move()

