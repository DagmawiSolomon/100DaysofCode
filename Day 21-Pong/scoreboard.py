from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Silkscreen", 30, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("#ffffff")
        self.speed(0)
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0

    def score(self):
        self.penup()
        self.clear()
        self.setx(-150)
        self.sety(250)
        self.write(self.player1_score, align=ALIGNMENT, font=FONT)

        self.setx(150)
        self.sety(250)
        self.write(self.player2_score, align=ALIGNMENT, font=FONT)

    def upgrade_score(self,paddle):
        if paddle == "left":
            self.player1_score += 1
            self.score()
        elif paddle == "right":
            self.player2_score += 1
            self.score()

