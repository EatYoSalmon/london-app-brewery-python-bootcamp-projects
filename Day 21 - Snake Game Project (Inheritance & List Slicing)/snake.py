from turtle import Turtle


# Constants of Snake class
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, color=None):
        """Sets snake color by passing in a string as argument;
        snake color defaults to white if left empty."""
        self.body = []
        self.color = color

        if self.color is None:
            self.color = "white"

        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        """Building the initial snake body; gets called automatically on object initialization."""
        for position in STARTING_COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        """Creates an instance of the Turtle object and appending it to the snake body."""
        seg = Turtle(shape="square")
        seg.color(self.color)
        seg.penup()
        seg.goto(position)

        self.body.append(seg)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        """Automates the movement by changing the coordinate of each segment[i] by having it
        move to the coordinate of the segment[i-1]."""
        for seg in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg - 1].xcor()
            new_y = self.body[seg - 1].ycor()
            self.body[seg].goto(new_x, new_y)

        self.head.fd(SNAKE_PACE)

    def up(self):
        """Changes direction and move towards the north of screen."""
        if self.head.heading() != DOWN and self.head.heading() != UP:
            self.head.setheading(UP)
        else:
            pass

    def down(self):
        """Changes direction and moves towards the south of screen."""
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(DOWN)

    def left(self):
        """Changes direction and move towards the east of screen."""
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes direction and move towards the west of screen."""
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)
