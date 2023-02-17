from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Silkscreen", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 200)
        self.color("white")
        self.write(f"Level: {self.level}", font=FONT, align=ALIGNMENT)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align=ALIGNMENT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)






