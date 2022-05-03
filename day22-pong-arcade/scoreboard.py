from turtle import Turtle, Screen


ALIGNMENT = "center"
FONT = ("Courier", 36, "normal")

class Scoreboard(Turtle):

    def __init__(self, screen):

        super().__init__()

        self.l_score = 0
        self.r_score = 0
        self.height = screen.window_height()

        self.painter = Turtle()

        self.painter.pu()
        self.painter.color("white")
        self.painter.hideturtle()

        self.hideturtle()
        self.pu()
        self.shape("square")
        self.color("HotPink")
        self.speed(0)
        self.pensize(4)
        self.goto(0, -1 * self.height/2)
        
        dash = 24
        for _ in range(self.height // dash):
            self.setheading(90)
            self.pd()
            self.fd(dash // 3)
            self.pu()
            self.fd(2 * (dash // 3))

        self.pu()
        self.setheading(0)
        
        self.write_score()


    def write_score(self):
        
        self.painter.goto(0, 240)
        self.painter.clear()
        self.painter.write(f"{self.l_score}      {self.r_score}", True, align=ALIGNMENT, font=FONT)


    def add_left(self):

        self.l_score += 1
        self.write_score()


    def add_right(self):

        self.r_score += 1
        self.write_score()


    def game_over(self):

        self.goto(0, 0)
        self.shapesize(12, 35)
        self.stamp()

        self.color("Black")
        if self.l_score > self.r_score:
            winner = "LEFT"
        elif self.r_score > self.l_score:
            winner = "RIGHT"

        self.write(f"!!--{winner} PLAYER WINS--!!", True, align=ALIGNMENT, font=FONT)



