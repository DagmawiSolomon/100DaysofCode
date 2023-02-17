from turtle import Turtle
from scoreboard import Scoreboard
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.hideturtle()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color("#ffffff")
            new_car.penup()
            random_y = random.randint(-190, 250)
            new_car.goto(360, random_y)
            new_car.showturtle()
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT






