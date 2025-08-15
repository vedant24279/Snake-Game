from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snakes()
        self.head = self.segments[0]

    def create_snakes(self):
        for posi in STARTING_POSITIONS:
            self.add_segment(posi)


    def add_segment(self,posi):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(posi)
        self.segments.append(new_snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[num - 1].xcor()
            y = self.segments[num - 1].ycor()
            self.segments[num].goto(x, y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


