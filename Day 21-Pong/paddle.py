from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.draw_paddle(pos)

    def draw_paddle(self,pos):
        self.shape("square")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("#ffffff")
        if pos == "left":
            self.goto(-320, 0)
        if pos == "right":
            self.goto(315, 0)

    def move_up(self):
        if self.ycor() < 250:
            y = self.ycor()
            y += 35
            self.sety(y)

    def move_down(self):
        if self.ycor() > -250:
            y = self.ycor()
            y -= 35
            self.sety(y)

