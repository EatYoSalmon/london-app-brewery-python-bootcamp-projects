from turtle import Turtle
from random import randint


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Ball(Turtle):

    def __init__(self):

        super().__init__()
        self.pace = 20

        self.penup()
        self.shape("circle")
        self.color("white")
        self.start_seed = randint(0, 1)
        if self.start_seed == 0:
            self.setheading(randint(120, 239))
        else:
            self.setheading(randint(300, 419) % 360)            
        self.goto(0, 0)
    

    def respawn(self, last_winner=str):
        
        self.pace = 20
        self.goto(0, 0)
        if last_winner == "right":
            self.setheading(randint(300, 419) % 360)
        elif last_winner == "left":
            self.setheading(randint(120, 239))


    def move(self):

        self.fd(self.pace)


    def bounce(self, mirror_angle=int):

        circ = 360

        impact_direction = (self.heading() + 180) % circ
        impact_angle = mirror_angle - impact_direction

        bounce_chaos = randint(-3, 3)
        bounce_angle = impact_angle + bounce_chaos
        bounce_direction = (mirror_angle + bounce_angle) % circ 

        self.setheading(bounce_direction)
        

    def is_hit(self):

        self.pace += 3

    # def bounce_heading(self, change):
    #     circ = 360
    #     angle = self.heading() + change
    #     circ_angle = None

    #     if angle < 0:
    #         circ_angle = circ + (angle % -circ)    
    #     else:
    #         circ_angle = angle % circ       

    #     self.setheading(circ_angle)

    # def wall_bounce(self):
    #     direction = self.heading()
    #     if self.ycor() > 280:
    #         if (direction >= UP and direction < LEFT):
    #             self.bounce_heading(90)
    #         elif (direction >= RIGHT and direction < UP):
    #             self.bounce_heading(-90)
    #     elif self.ycor() < -280: 
    #         if (direction >= LEFT and direction < DOWN):
    #             self.bounce_heading(-90)
    #         elif (direction >= DOWN and direction < 360):
    #             self.bounce_heading(90)

    # def paddle_bounce(self, paddle):
    #     direction = self.heading()
    #     if self.distance(paddle) <= 10:
    #         if (direction < UP):
    #             self.bounce_heading(90)
    #         elif (direction > DOWN):
    #             self.bounce_heading(-90)