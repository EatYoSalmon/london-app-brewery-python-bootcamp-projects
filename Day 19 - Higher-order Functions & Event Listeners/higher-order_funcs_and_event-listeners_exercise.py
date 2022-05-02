from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fd():
    tim.forward(10)

def move_bk():
    tim.backward(10)

def turn_cw():
    tim.right(30)

def turn_ccw():
    tim.left(30)

def clear_and_center():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_fd)
screen.onkeypress(key="s", fun=move_bk)
screen.onkeypress(key="d", fun=turn_cw)
screen.onkeypress(key="a", fun=turn_ccw)
screen.onkeypress(key="c", fun=clear_and_center)

screen.exitonclick()