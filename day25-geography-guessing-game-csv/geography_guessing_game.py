import turtle
import pandas as pd
from pathlib import Path


parent_dir = str(Path(__file__).parent.resolve())
image = "/blank_states_img.gif"

df = pd.read_csv(parent_dir + "/50_states.csv")
states = df.state.to_list()

screen = turtle.Screen()
screen.title("USA States Guessing Game")
screen.addshape(parent_dir + image)

turtle.shape(parent_dir + image)

writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)
writer.penup()

state_coor = {}
for state in states:
    state_row = df[df.state == state]
    state_coor[state] = (int(state_row.x), int(state_row.y))

score = 0
guessed_states = []

while score < 50:

    if score < 1:
        input_title = "Guess the State"
    else:
        input_title = f"{score}/50 States Correct"

    answer_state = screen.textinput(
        title=input_title,
        prompt="What's another state's name?"
    ).title()

    if answer_state == "Exit":
        break

    if (answer_state in states) and (answer_state not in guessed_states):

        writer.goto(state_coor[answer_state])
        writer.write(answer_state, align="center")

        guessed_states.append(answer_state)
        score += 1

if score < 50:

    remaining_states = states.copy()
    for state in guessed_states:
        remaining_states.remove(state)

    to_learn = pd.Series(remaining_states)
    to_learn.to_csv(parent_dir + "/states_to_learn.csv")

else:

    player_name = screen.textinput(
        title="Congratulation!",
        prompt="You've completed the game! Enter your name to be claim your place among the Geo-Masters."
    )

screen.mainloop()
