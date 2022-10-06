from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
player_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "OrangeRed", "gold", "green", "blue", "purple"]
starts = [-160, -96, -32, 32, 96, 160]
turtle_racers = []
is_race_on = False

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, starts[i])
    turtle_racers.append(new_turtle)

if player_bet:
    is_race_on = True

while is_race_on:

    for racer in turtle_racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == player_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)

screen.exitonclick()
