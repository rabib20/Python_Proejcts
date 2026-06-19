from turtle import Turtle
import time
class paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(position)

        self.move_right = False
        self.move_left = False

    def start_right(self):

        self.move_right = True

    def stop_right(self):

        self.move_right = False

    def start_left(self):

        self.move_left = True

    def stop_left(self):

        self.move_left = False