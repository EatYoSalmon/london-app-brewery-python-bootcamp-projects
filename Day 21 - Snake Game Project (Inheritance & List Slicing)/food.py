from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, color):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("white")

        self.color(color)
        if self.color() is None:
            self.color("white")

        self.refresh()

    def refresh(self):
        random_x = random.randint(-265, 265)
        random_y = random.randint(-265, 265)
        self.goto(random_x, random_y)
