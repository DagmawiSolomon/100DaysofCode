from turtle import Turtle


class Background(Turtle):

    def __init__(self):
        super(Background, self).__init__()
        self.width(8)
        self.color("#ffffff")
        self.speed(0)
        self.hideturtle()

    def draw_half_way_line(self):
        self.goto(0, 300)
        self.setheading(270)
        while self.ycor() > -300:
            self.forward(150)
