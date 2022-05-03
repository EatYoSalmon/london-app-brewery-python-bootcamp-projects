from turtle import Turtle


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):
    def __init__(self, xpos, ypos) -> None:
        super().__init__()
        self.penup()
        self.setheading(UP)
        self.color("white")
        self.shape("square")

        self.resizemode("user")
        self.goto(xpos, ypos)
        self.shapesize(1, 5, 0)

    def move_up(self):
        self.fd(25)

    def move_down(self):
        self.bk(25)
