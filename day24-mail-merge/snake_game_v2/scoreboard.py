from turtle import Turtle
from pathlib import Path

CONTAINER_PATH = Path(__file__).parent.resolve()
DATA_PATH = str(CONTAINER_PATH) + "/data.txt"
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.game_score = 0

        with open(DATA_PATH, "r") as file:
            current_high_score = int(file.read())

        self.high_score = current_high_score

        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.game_score}, High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.game_score += 1
        self.write_score()

    def update_high_score(self):
        with open(DATA_PATH, "w") as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score
            self.update_high_score()
        self.game_score = 0
        self.write_score()


