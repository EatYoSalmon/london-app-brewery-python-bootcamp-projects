from turtle import Turtle
from random import randint, randrange, choice, shuffle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class CarManager:
    # Attr: speed_limit, cars
    # Each car in its cars attr is a list containing 2 turtle objects
    # The speed_limit attr starts at the constant STARTING_MOVE_DISTANCE and increases by
    # the constant MOVE_INCREMENT every time play pass a level.

    # Mthd: manage(self), new_car(self), auto_del() drive(self), add_level(self)
    # Generates new cars continuously, increments them to left side, deletes off-screen
    # ones, and increases speed_limit attr by the constant MOVE_INCREMENT.

    def __init__(self):

       self.speed_limit = STARTING_MOVE_DISTANCE
       self.cars = []


    def manage_v1(self):
        """Generates, moves, deletes, and manages quantity and pace of cars;
        The main orchestrating method of a CarManager object.
        
        v1: Generation algorithm is randomized probabilistically upon each screen refresh:
        There's a 10% chance of more cars being added at every refresh;
        Single car generation has 60% drop rate;
        Double has 30% drop rate
        Tripple has 10% drop rate"""        

        gen_seed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        gen_type = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3]

        shuffle(gen_seed)
        is_gen = bool(choice(gen_seed))
        
        if is_gen:
            shuffle(gen_type)
            gen_quan = choice(gen_type)
            
            gen_cars = []
            for n in range(gen_quan):
                gen_cars.append(self.new_car())
            
            self.cars.extend(gen_cars)

        self.drive()
        self.auto_del()  


    def new_car(self):
        """Generates a car as a list of containing 2 Turtle objects;
        Returns the car as a list"""

        rand_y_spawn = randint(-280, 280)
        rand_color = choice(COLORS)

        car_front = Turtle()
        car_front.pu()
        car_front.goto(300, rand_y_spawn)
        car_front.setheading(LEFT)
        car_front.shape("square")
        car_front.color(rand_color)

        car_back = car_front.clone()
        car_back.goto(car_front.xcor() + 20, car_front.ycor())

        car = [car_front, car_back]

        return car


    def drive(self):
        """Moves the cars across from the right to the left of screen;"""

        for car in self.cars:
            car[0].fd(self.speed_limit)
            car[1].fd(self.speed_limit)


    def auto_del(self):
        """Automatically deletes cars that are off the screen."""

        for car in self.cars:
            if car[0].xcor() < -320:
                car[0].ht()
                car[1].ht()
                self.cars.remove(car)

    
    def add_level(self):
        """Increases speed_limit of the cars, making the game harder."""

        self.speed_limit += MOVE_INCREMENT

