from turtle import Turtle

class Scoreboards(Turtle):
        def __init__(self):
            super().__init__()

            self.color("blue")
            self.penup()
            self.up_score = 0
            self.down_score = 0

            self.hideturtle()
            self.update_scoreboard()

        def update_scoreboard(self):
            self.goto(0, -40)
            self.write(f"Player 1: {self.up_score}", align="center", font=("Arial", 24, "normal"))

            self.goto(0, 40)
            self.write(f"Player 2: {self.down_score}", align="center", font=("Arial", 24, "normal"))

        def increase_up_scoreboard(self):

            self.up_score += 1
            self.clear()
            self.update_scoreboard()

        def increase_down_scoreboard(self):

            self.down_score +=1
            self.clear()
            self.update_scoreboard()

        def Game_Over(self):
            self.goto(0,0)
            self.write("Game Over", align="center", font=("Arial", 24, "normal"))