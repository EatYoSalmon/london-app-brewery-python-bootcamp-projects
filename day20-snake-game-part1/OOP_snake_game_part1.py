from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Grich Snake Game")
screen.tracer(0)

# Initialize a Snake object and construct the snake body
snake = Snake("IndianRed1")

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

    # Control screen refresh rate for smooth animation
    screen.update()
    time.sleep(0.1)

    # Move the snake head forward by 20px and each segment[i] in the snake.body
    # by having it replace the coordinates of the segment[i-1]
    snake.move()

screen.exitonclick()
