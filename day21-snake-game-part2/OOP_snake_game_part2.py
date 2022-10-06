from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Grich Snake Game")
screen.tracer(0)

# Initialize a Snake object and construct the snake body
snake = Snake("MediumSlateBlue")
food = Food("HotPink")
scoreboard = Scoreboard()

# Put focus on the screen object and have it listen for keystrokes to control
# the snake movement using higher-order functions.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Automates the snake movement
is_game_over = False
while not is_game_over:

    # Controls screen refresh rate for smooth animation
    screen.update()
    time.sleep(0.1)

    # Moves the snake head forward by 20px and each segment[i] in the snake.body
    # by having it replace the coordinates of the segment[i-1]
    snake.move()

    # Detects collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detects collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_over = True
        scoreboard.game_over()

    # Detects collision with tail.
    for seg in snake.body[1:]:
        if snake.head.distance(seg) < 10:
            is_game_over = True
            scoreboard.game_over()


screen.exitonclick()
