from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

window = Screen()
window.setup(600, 600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")

gameIsOn = True
while gameIsOn:
    window.update()
    time.sleep(0.2)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.otherEnd()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameIsOn = False
            scoreboard.gameOver()
            
window.exitonclick()