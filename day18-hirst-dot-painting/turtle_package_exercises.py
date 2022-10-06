from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()
tim.color("firebrick1")

# Challenge 1: Square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# import heroes
# print(heroes.gen())

# Challenge 2: Dashed Line
# for _ in range(50):
#     tim.fd(4)
#     tim.pu()
#     tim.fd(4)
#     tim.pd()

# Challenge 3: Draw Polygons in Different Colors

# def draw_shape(num_sides):
#     for _ in range(0, num_sides):
#         tim.forward(100)
#         tim.right(360/num_sides)

# colors = ["MediumBlue", "purple", "red", "orange", "yellow", "MidnightBlue", "magenta", "turquoise1", "NavajoWhite3"]

# for polygon in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(polygon)

# Challenge 4: Draw a Random Walk
# dir_colors = {
#     0: "SpringGreen",
#     60: "Turquoise",
#     300: "Turquoise",
#     120: "BlueViolet",
#     240: "BlueViolet",
#     180: "DeepPink"
# }
# tim.pensize(10)
# tim.speed(10)

# for _ in range(200):
#     dir = random.randrange(0, 360, 60)
#     tim.color(dir_colors[dir])
#     tim.setheading(dir)
#     tim.forward(40)

# Challenge 5: Random RGB Colors
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     randcolor = (r, g, b)
#     return randcolor

# tim.pensize(10)
# tim.speed(10)

# for _ in range(200):
#     dir = random.randrange(0, 360, 60)
#     tim.color(random_color())
#     tim.setheading(dir)
#     tim.forward(40)

# Challenge 6: Make a Spirograph
tim.speed(0)
def make_spirograph(gap):
    for i in range(360//gap):
        tim.circle(200)
        tim.setheading(tim.heading() + gap)

make_spirograph(10)

t.done()