from re import I
from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):

    def __init__(self):

        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)

        self.setheading(UP)
        self.color("black")
        self.shape("turtle")


    def cross(self):
        """Moves player up by constant MOVE_DISTANCE"""
            
        self.goto(0, (self.ycor() + MOVE_DISTANCE))


    def go_back_if_pass(self):
        """Returns True and resets player to starting position if level is passed;
        Returns False and do nothing if not."""

        is_passed = False

        if not self.ycor() >= FINISH_LINE_Y:
            return is_passed
                
        self.goto(STARTING_POSITION)
        is_passed = True

        return is_passed

    def got_hit(self, cars):
        """Detects if player has been hit by a car;
        Returns True if player got hit, False if not."""

        collision = False

        for i, car in enumerate(cars):

            # pos1 = car[0].pos()
            # pos2 = car[1].pos()
            # print(f"Detecting if hit with car#{i}: {pos1} & {pos2}.")

            if self.distance(car[0]) < 12 or self.distance(car[1]) < 12:
                    
                collision = True
                return collision
                



