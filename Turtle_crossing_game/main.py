import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
score_board = Scoreboard()
screen.listen()
screen.onkeypress(player.start_up, "w")
screen.onkeyrelease(player.stop_up, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.move()
    carManager.create_cars()
    carManager.move_car()

    if player.ycor() > 290:
        player.goto(0, -280)
        carManager.increase_car_speed()
        score_board.level_up()

    if 1 <= score_board.level <= 2:
        carManager.create_cars()

    elif 3 <= score_board.level <= 4:
        carManager.create_cars_level_upto4()

    elif 5 <= score_board.level <= 6:
        carManager.create_cars_level_from5()

    elif 7 <= score_board.level <= 8:
        carManager.create_cars_level_from7()

    else:  # level >= 9
        carManager.create_cars_level_from9()

    for car in carManager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over(carManager.car_count)

screen.exitonclick()
