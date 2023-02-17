import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
colormode(255)
timmy.penup()
timmy.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (140, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 40), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

dot_count = 0
angle = [0, 90, 180, 270]

def draw_dot(num_of_dots):
    count = 1
    layer = 0
    for _ in range(num_of_dots):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(40)
        count += 1
        if count > 10:
            if layer % 2 == 0:
                timmy.setheading(90)
                timmy.forward(40)
                timmy.setheading(180)
                timmy.forward(40)
            else:
                timmy.setheading(90)
                timmy.forward(40)
                timmy.setheading(0)
                timmy.forward(40)
            layer += 1
            count = 1




draw_dot(100)


screen = Screen()
screen.exitonclick()