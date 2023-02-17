from turtle import Turtle, Screen
import time

SPEED = 15
SCREEN = Screen()
SCREEN.addshape("assets/bullet.gif")


class Bullet:

    def __init__(self, ship_x):
        self.bullet_list = []
        self.bullet = Turtle()
        self.bullet.speed(0)
        self.x_cor = ship_x
        self.bullet.shape("assets/bullet.gif")
        self.bullet.penup()
        self.bullet.goto(self.x_cor, 0)
        self.bullet_list.append(self.bullet)

    def fire(self):
        y_cor = -265
        while y_cor < 380:
            y_cor += SPEED
            self.bullet.sety(y_cor)
        if y_cor > 380:
            self.bullet = 0

