from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.game_score = 0

        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.game_score}", True, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.game_score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("!!--GAME OVER--!!", True, align=ALIGNMENT, font=FONT)

