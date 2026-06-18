import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed_value = STARTING_MOVE_DISTANCE
        self.car_count = 0

    def _create_single_car(self):
        self.car_count += 1

        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))

        random_y = random.randint(-250, 250)
        car.goto(300, random_y)

        self.all_cars.append(car)
        print(f"car_count = {self.car_count}")

    def create_cars(self):
        if random.randint(1, 6) == 1:
            self._create_single_car()

    def create_cars_level_upto4(self):
        if random.randint(1, 4) == 1:
            self._create_single_car()

    def create_cars_level_from5(self):
        if random.randint(1, 3) == 1:
            self._create_single_car()

    def create_cars_level_from7(self):
        if random.randint(1, 2) == 1:
            self._create_single_car()

    def create_cars_level_from7(self):
        self._create_single_car()

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed_value)

    def increase_car_speed(self):
        self.car_speed_value += MOVE_INCREMENT