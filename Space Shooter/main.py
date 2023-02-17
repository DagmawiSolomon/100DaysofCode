import time
from turtle import Screen
from ship import SpaceShip
from Bullet import Bullet
from Enemy import Enemy


screen = Screen()
screen.bgcolor("#3c2c3c")
screen.listen()
screen.setup(600, 725)


space_ship = SpaceShip()
space_ship.create_ship()

screen.onkey(space_ship.move_right, "Right")
screen.onkey(space_ship.move_left, "Left")


bullets_list = []
def fire_bullets():
    bullet = Bullet(space_ship.ship_xcor)
    bullet.fire()
    bullets_list.append(bullet)


screen.onkey(fire_bullets, "space")

game_on = True
enemy = Enemy()

for bullet in bullets_list:
    print(bullet.distance(enemy))
    if bullet.distance(enemy) > 10:
        print("dead")

while game_on:
    enemy.spawn_enemy()
    enemy.move()

screen.exitonclick()