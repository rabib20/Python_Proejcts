from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player (Turtle):

    def __init__(self):

        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.color("violet")

        self.go_up = False

    def start_up(self):
        self.go_up = True

    def stop_up(self):
        self.go_up = False

    def move(self):
        if self.go_up:
            self.forward(MOVE_DISTANCE)