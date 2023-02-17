import json
import turtle
from turtle import Screen



countries_dict = {}

game_on = True




def check_country():
    global game_on
    z = turtle.Turtle(shape="circle")
    z.hideturtle()
    z.penup()
    user_guess = screen.textinput("Guess the country:", "Country:")
    if user_guess.lower() == "end":
        game_on = False
    else:
        if user_guess in j:
            cor = j[user_guess]
            print(user_guess)
            z.goto(cor[0], cor[1])
            z.color("#9bdeac")

    z.showturtle()


# def detect_hover(x, y):
#     if x == j[]


while game_on:
    check_country()

turtle.onscreenclick(detect_hover)
screen.mainloop()


