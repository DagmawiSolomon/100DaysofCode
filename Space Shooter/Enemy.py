from turtle import Turtle, Screen
import random

SPEED = 5
SCREEN = Screen()
SCREEN.addshape("assets/enemy.gif")


class Enemy:

    def __init__(self):
        self.enemies_list = []
        self.y = 0
        self.move()

    def spawn_enemy(self):
        self.enemy = Turtle()
        self.y = self.enemy.ycor()
        self.enemy.penup()
        self.enemy.hideturtle()
        self.enemy.shape("assets/enemy.gif")
        self.enemy.setheading(270)
        self.enemy.goto(random.randint(-300, 300), 525)
        self.enemy.showturtle()
        self.enemies_list.append(self.enemy)

    def move(self):
        for enemy in self.enemies_list:
            while enemy.ycor() > -525:
                enemy.forward(1)





