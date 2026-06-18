from turtle import Turtle
from car_manager import CarManager

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()

            self.level = 1
            self.color = "black"
            self.hideturtle()
            self.penup()
            self.goto(-280,250)
            self.update_Scoreboard()

        def update_Scoreboard(self):
            self.clear()
            self.write(f"Level: {self.level}", align="left", font=FONT)


        def level_up(self):
            self.level += 1
            self.update_Scoreboard()

        def game_over(self, car_count):
            self.goto(0, 0)
            final_score = car_count * self.level
            self.write(f" Game over! your Score is {final_score}", align="center", font=FONT)
