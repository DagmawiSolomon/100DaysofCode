import json
import turtle
from turtle import Screen

screen = Screen()
screen.setup(width=817,height=700)
screen.title("Name the country")
image = "images/map.gif"
screen.addshape(image)
screen.listen()

turtle.shape(image)


countries_dict = {}


def coordinate_genarator(x,y):
    z = turtle.Turtle(shape="circle")
    z.hideturtle()
    z.penup()
    z.color("#323031")
    z.goto(x, y)
    z.showturtle()
    country_name = input("Enter country name: ")
    countries_dict[country_name] = (x,y)
    print(countries_dict)





def save_as_csv():
    with open("countries.json","w") as file:
        json.dump(countries_dict, file)
    print("dumped")


turtle.onscreenclick(coordinate_genarator)
turtle.onkey(save_as_csv, "space")

screen.mainloop()