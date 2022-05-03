from turtle import Turtle, Screen, left
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360
TRUE_RIGHT = 0
SCORE_LIMIT = 2

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
board = Scoreboard(screen)

screen.listen()
screen.onkey(r_paddle.move_up, "i")
screen.onkey(r_paddle.move_down, "k")
screen.onkey(l_paddle.move_up, "e")
screen.onkey(l_paddle.move_down, "d")

is_game_over = False
while is_game_over is False:
    time.sleep(0.1)
    screen.update()
    ball.move()


    if ball.ycor() > 290:
        ball.bounce(DOWN)

    elif ball.ycor() < -290:
        ball.bounce(UP)


    if ball.xcor() > 315 and ball.distance(r_paddle) <= 50:
        ball.bounce(RIGHT)
        ball.is_hit()

    elif ball.xcor() < - 315 and ball.distance(l_paddle) <= 50:
        ball.bounce(LEFT)
        ball.is_hit()


    if ball.xcor() > 380:
        board.add_left()
        ball.respawn("left")
        screen.update()
        time.sleep(3)

    elif ball.xcor() < -380:
        board.add_right()
        ball.respawn("right")
        screen.update()
        time.sleep(3)


    if board.r_score >= SCORE_LIMIT or board.l_score >= SCORE_LIMIT:
        is_game_over = True
        board.game_over()
        screen.update()


screen.exitonclick()