import turtle
from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

ray = Turtle()
turtle.colormode(255)
angle = [0, 90, 180, 270]
ray.width(5)
ray.speed("fastest")


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_tuple = (red, green, blue)
    return color_tuple


# for _ in range(100):
#     ray.forward(30)
#     ray.color(random_color())
#     ray.setheading(random.choice(angle))


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        ray.color(random_color())
        ray.circle(100)
        ray.setheading(ray.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
