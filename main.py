from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# Classic Snake Game written in Python using Turtle module. 

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Create Objects
snake = Snake()
snake.create_snake()
food = Food()
scoreboard = Scoreboard()

#bind key to functions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #Move Snake
    snake.move()
    
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280) :
        scoreboard.reset()
        snake.reset()

    #detect collsiion with tail
    for segment in snake.segments[1:]: 
        if (snake.head.distance(segment) < 10):
            scoreboard.reset()
            snake.reset()

screen.exitonclick()