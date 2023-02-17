from turtle import Turtle, Screen

SPEED = 10
SCREEN = Screen()
SCREEN.addshape("assets/ship.gif")
x = 0

class SpaceShip:

    def __init__(self):
        self.space_ship = Turtle()
        self.space_ship.speed(0)
        self.ship_xcor = 0

    def create_ship(self):
        self.space_ship.shape("assets/ship.gif")
        self.space_ship.shapesize(0.5, 0.5)
        self.space_ship.color("#FFFFFF")
        self.space_ship.setheading(90)
        self.space_ship.penup()
        self.space_ship.goto(0, -300)

    def move_right(self):
        if self.ship_xcor < 250:
            self.ship_xcor += 15
            self.space_ship.setx(self.ship_xcor)

    def move_left(self):
        if self.ship_xcor > -250:
            self.ship_xcor -= 15
            self.space_ship.setx(self.ship_xcor)




