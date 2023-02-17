from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(50)


def move_backward():
    tim.backward(50)


def turn_counterclockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_drawing():
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()

# A - counterclockwise/left
# D - clockwise/right
# c- clear
