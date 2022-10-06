import turtle as tt
import random


class HirstCanvas:

    def __init__(self, num_col, num_row, gap_size, dot_size, rgb_list):
        """To construct an instance of HirstCanvas, pass in 5 arguments to
        initialize the object.
        num_col: number of columns
        num_row: number of rows
        gap_size: the size of the gaps between each dots
        dot_size: the size of each dot
        rgb_list: a list containing rgb values as tuples (r, g, b)
        """
        self.dot = dot_size
        self.gap = gap_size
        self.col = num_col
        self.row = num_row
        self. palette = rgb_list

        self.x_dim = {
            "dim": self.gap * (self.col - 1),
            "left": -1 * ((self.gap * (self.col - 1)) / 2),
            "right": (self.gap * (self.col - 1)) / 2,
        }

        self.y_dim = {
            "dim": self.gap * (self.row - 1),
            "up": self.gap * (self.row - 1) / 2,
            "low": -1 * (self.gap * (self.row - 1) / 2),
        }

        self.corner = {
            "ll": (self.x_dim["left"], self.y_dim["low"]),
            "ul": (self.x_dim["left"], self.y_dim["up"]),
            "lr": (self.x_dim["right"], self.y_dim["low"]),
            "ur": (self.x_dim["right"], self.y_dim["up"]),

        }

    def paint_dots_hor(self, painter, start):
        """Uses a Turtle object from the turtle module to dot-paint the canvas horizontally by passing in the turtle object, and painter's start position as arguments.
        return: None
        painter: a turtle object
        start: the start positions;
            'll' for lower left corner,
            'ul' for upper left corner
            'lr' for lower right corner,
            'ur' for upper right corner.
        """
        painter.speed(0)
        painter.pu()
        painter.goto(self.corner[start])

        for row in range(self.row):

            for col in range(self.col):
                painter.dot(self.dot, random.choice(hirst_colors))

                x_pos = painter.pos()[0]
                painter.goto(x_pos + self.gap if start == "ll" or start == "ul" else x_pos - self.gap, painter.pos()[1])


            y_pos = painter.pos()[1]
            if start == "ll" or start == "lr":
                painter.goto(self.x_dim["left"] if start == "ll" else self.x_dim["right"], (y_pos + self.gap))
            else:
                painter.goto(self.x_dim["left"] if start == "ul" else self.x_dim["right"], (y_pos - self.gap))

    def paint_dots_ver(self, painter, start):
        """Uses a Turtle object from the turtle module to dot-paint the canvas vertically by passing in the turtle object, and painter's start position as arguments.
        return: None
        painter: a turtle object
        start: the start positions;
            'll' for lower left corner,
            'ul' for upper left corner
            'lr' for lower right corner,
            'ur' for upper right corner.
        """
        painter.speed(0)
        painter.pu()
        painter.goto(self.corner[start])

        for col in range(self.col):

            for row in range(self.row):
                painter.dot(self.dot, random.choice(hirst_colors))

                y_pos = painter.pos()[1]
                painter.goto(painter.pos()[0], y_pos + self.gap if start == "ll" or start == "lr" else y_pos - self.gap)


            x_pos = painter.pos()[0]
            if start == "ll" or start == "ul":
                painter.goto((x_pos + self.gap), self.y_dim["up"] if start == "ul" else self.y_dim["low"])
            else:
                painter.goto((x_pos - self.gap), self.y_dim["up"] if start == "ur" else self.y_dim["low"])


# def random_color():
#     """Return a random color as a tuple of RGB values (r, g, b)"""
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     randcolor = (r, g, b)
#
#     return randcolor


tt.colormode(255)
timmy = tt.Turtle()
timmy.hideturtle()

hirst_colors = [
    (221, 157, 105), (238, 217, 199), (97, 169, 213), (234, 65, 80), (218, 231, 225),
    (229, 118, 144), (238, 201, 97), (125, 189, 164), (29, 121, 164), (234, 73, 59),
    (178, 182, 215), (36, 115, 70), (24, 38, 79), (168, 210, 179), (234, 158, 179),
    (104, 63, 85), (169, 55, 39), (26, 133, 233), (240, 158, 148), (39, 153, 196),
    (27, 93, 63), (54, 169, 135), (76, 73, 27), (31, 72, 37), (4, 81, 109),
    (20, 60, 113), (153, 206, 217), (186, 157, 64)]

hirst_dot_painting = HirstCanvas(5, 5, 70, 20, hirst_colors)

hirst_dot_painting.paint_dots_hor(tt, "ll")
tt.clearscreen()
tt.colormode(255)

hirst_dot_painting.paint_dots_hor(tt, "ul")
tt.clearscreen()
tt.colormode(255)

hirst_dot_painting.paint_dots_hor(tt, "lr")
tt.clearscreen()
tt.colormode(255)

hirst_dot_painting.paint_dots_hor(tt, "ur")
tt.clearscreen()
tt.colormode(255)


hirst_dot_painting.paint_dots_ver(tt, "ll")
tt.clearscreen()
tt.colormode(255)

hirst_dot_painting.paint_dots_ver(tt, "ul")
tt.clearscreen()
tt.colormode(255)

hirst_dot_painting.paint_dots_ver(tt, "lr")
tt.clearscreen()
tt.colormode(255)

hirst_dot_painting.paint_dots_ver(tt, "ur")
tt.clearscreen()
tt.colormode(255)


tt.done()
