import turtle
from turtle import Screen
import pandas
ALIGNMENT = "center"
FONT = ("Roboto", 6, "bold")

screen = Screen()
screen.title("Name the states")
screen.setup(725,491)
image = "img.gif"
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
game_on = True
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_state)}/{len(all_states)}", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=FONT)

turtle.mainloop()

