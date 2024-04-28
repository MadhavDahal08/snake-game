from snake import Snake
import time
from turtle import Screen
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(snake.up, "Up")

screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.calculate_score()


    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()



    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()


















screen.exitonclick()