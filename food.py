from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.75,stretch_len=0.75)
        self.penup()
        self.refresh()

    def refresh(self):
        x_pos = random.randint(-280,280)
        y_pos = random.randint(-280,280)
        self.goto(x=x_pos,y=y_pos)