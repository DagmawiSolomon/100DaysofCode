from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("#ffffff")
        self.penup()
        self.hideturtle()
        self.setheading(90)

    def go_to_start(self):
        self.goto(0, -200)
        self.showturtle()

    def move(self):
        y = self.ycor()
        y += 20
        self.sety(y)



