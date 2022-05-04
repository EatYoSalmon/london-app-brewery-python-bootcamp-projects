from turtle import Turtle


FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    # Attr: level
    # Mthd: add_level(self), game_over(self)

    def __init__(self):
        
        self.level = 1
        super().__init__()

        self.ht()
        self.pu()
        self.goto(-300, 300)
        self.color("black")

        self.write_score()


    def write_score(self):

        self.clear()
        self.goto(-280, 270)
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def add_level(self):

        self.level += 1
        self.write_score()


    def game_over(self):

        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
