import json
import turtle
from turtle import Screen

screen = Screen()
screen.setup(width=820, height=700)
screen.title("Name the country")
image = "images/map.gif"
screen.addshape(image)
screen.listen()

turtle.shape(image)

GAME_ON = True

class NameTheCountrty:


    def __init__(self):
        self.file = open("countries.json", "r")
        self.countries_file = json.load(self.file)
        self.guess = ""

    def check_country(self):
            user_guess = screen.textinput("Guess the country:", "Country:")
            self.guess = user_guess
            if self.guess.lower() == "end":
                global GAME_ON
                GAME_ON = False
            else:
                if self.guess in self.countries_file:
                    cor = self.countries_file[self.guess]
                    name = turtle.Turtle()
                    name.hideturtle()
                    name.penup()
                    name.goto(cor[0]+5, cor[1])
                    name.write(self.guess)


c = NameTheCountrty()
while GAME_ON:
    c.check_country()



screen.mainloop()