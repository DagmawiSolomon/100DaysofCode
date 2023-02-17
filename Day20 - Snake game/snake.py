from turtle import Turtle
move_distance = 20
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.seg_coordinate = []
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in POSITION:
            self.add_segment(i)

    def add_segment(self, i):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(i)
        self.seg_coordinate.append(new_segment.pos())
        self.segments.append(new_segment)

    def extend(self):

        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.seg_coordinate) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

