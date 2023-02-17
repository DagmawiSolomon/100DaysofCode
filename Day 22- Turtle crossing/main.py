import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
screen = Screen()
screen.listen()
screen.setup(width=700, height=500)
screen.tracer(0)
screen.bgcolor("#323031")
screen.title("Turtle crossing ")

scoreboard = Scoreboard()


player = Player()
player.go_to_start()
screen.onkey(player.move, "Up")

car = Cars()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for x in car.all_cars:
        if x.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 215:
        player.go_to_start()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        car.level_up()




screen.exitonclick()