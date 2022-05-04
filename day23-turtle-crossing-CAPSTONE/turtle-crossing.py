import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Initializes a Screen object.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initializes Player, CarManager, and Scoreboard objects.
player = Player()
manager = CarManager()
board = Scoreboard()

# Sets up the main game loop.
is_game_over = False
screen.listen()
while is_game_over is False:

    # Sets framerate at 0.1 sec and manually refreshes Screen object
    time.sleep(0.1)
    screen.update()

    # Main looping section; all the background processes of the game.
    screen.onkey(player.cross, "Up")
    manager.manage_v2()

    # Triggers if player passes current level.
    if player.go_back_if_pass():

        board.add_level()
        manager.add_speed()

    # Triggers if player got hit by a car.
    if player.got_hit(manager.cars):

        is_game_over = True
        board.game_over()
                

screen.exitonclick()
