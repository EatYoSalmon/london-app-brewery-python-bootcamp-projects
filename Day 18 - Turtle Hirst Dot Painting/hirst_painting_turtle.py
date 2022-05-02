# import colorgram
#
# colors = colorgram.extract("painting_colors.jpeg", 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)

from turtle import Turtle
import turtle as tt
import random

hirst_colors = [
    (221, 157, 105), (238, 217, 199), (97, 169, 213), (234, 65, 80), (218, 231, 225),
    (229, 118, 144), (238, 201, 97), (125, 189, 164), (29, 121, 164), (234, 73, 59),
    (178, 182, 215), (36, 115, 70), (24, 38, 79), (168, 210, 179), (234, 158, 179),
    (104, 63, 85), (169, 55, 39), (26, 133, 233), (240, 158, 148), (39, 153, 196),
    (27, 93, 63), (54, 169, 135), (76, 73, 27), (31, 72, 37), (4, 81, 109),
    (20, 60, 113), (153, 206, 217), (186, 157, 64)]

tt.colormode(255)

timmy = Turtle()
timmy.speed(0)

dot_size = 20
dot_gap = 70
num_col = 10
num_row = 10

x_dim = {
    "dim": dot_gap * (num_col - 1),
    "left": -1 * ((dot_gap * (num_col - 1)) / 2),
    "right": (dot_gap * (num_col - 1)) / 2,
}
y_dim = {
    "dim": dot_gap * (num_row - 1),
    "up": dot_gap * (num_row - 1) / 2,
    "low": -1 * (dot_gap * (num_row - 1) / 2),
}

low_left = (x_dim["left"], y_dim["low"])
up_left = (x_dim["left"], y_dim["up"])
low_right = (x_dim["right"], y_dim["low"])
up_right = (x_dim["right"], y_dim["up"])

timmy.pu()
timmy.goto(low_left)

for row in range(num_row):

    for col in range(num_col):
        timmy.dot(dot_size, random.choice(hirst_colors))
        x_pos = timmy.pos()[0]
        timmy.goto(x_pos + dot_gap, timmy.pos()[1])

    y_pos = timmy.pos()[1]
    timmy.goto(x_dim["left"], (y_pos + dot_gap))

tt.done()
