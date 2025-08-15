from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")
is_game_on = True
while is_game_on:
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        is_game_on = False
        scoreboard.game_over()

    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            is_game_on = False
            scoreboard.game_over()




















screen.exitonclick()