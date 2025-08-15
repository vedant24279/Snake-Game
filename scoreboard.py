from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score= 0
        self.color("White")
        self.penup()
        self.goto(0,265)
        self.speed("fastest")
        self.scoreboard()


    def scoreboard(self):
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 20, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.scoreboard()