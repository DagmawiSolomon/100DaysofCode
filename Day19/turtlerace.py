from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtle = []
j = -100
for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle. penup()
    new_turtle.color(i)
    new_turtle.goto(x=-230, y=j)
    j = j + 50
    all_turtle.append(new_turtle)



if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()

