from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("arrow")
num_sides = 3
color = ["red","orange","yellow","green","blue","indigo","purple","cyan","cornsilk"]
while num_sides < 11:
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(360/num_sides)
    timmy.color(random.choice(color))
    num_sides += 1


screen = Screen()
screen.exitonclick()