from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Grich Snake Game")
screen.tracer(0)

# Build the Snake Body; append Turtle objects to a list via a for-loop
snake_body = []
x_crdn = 0

for seg in range(3):

    seg = Turtle(shape="square")
    seg.color("white")
    seg.penup()
    seg.goto(x_crdn, 0)

    snake_body.append(seg)
    x_crdn -= 20


# Animate & *Automate* Movement of the Snake;
    # use sleep() from time module to control the screen refresh rate for smoother animation;
    # the screen.update() controls when the screen object refresh if not called within a script, it
    # defaults to runtime-speed
is_game_over = False
while not is_game_over:

    screen.update()
    time.sleep(0.1)

    # Automate the movement by changing the coordinate of each segment[i] by having it move to the coordinate
    # of the segment[i-1].
    for seg in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[seg - 1].xcor()
        new_y = snake_body[seg - 1].ycor()
        snake_body[seg].goto(new_x, new_y)

    snake_body[0].fd(20)
    snake_body[0].right(90)

screen.exitonclick()
