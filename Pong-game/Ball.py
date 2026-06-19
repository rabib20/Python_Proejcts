from turtle import Turtle

class ball(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5


    def ball_move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_x(self):

        if self.xcor() > 280 or self.xcor() < -280:

            self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

        if self.x_move > 0:
            self.x_move += 3
        else:
            self.x_move -= 3

        if self.y_move > 0:
            self.y_move += 3
        else:
            self.y_move -= 3

    def ball_out(self):

        self.goto(0,0)
        self.x_move = 5
        if self.y_move > 0:
            self.y_move = -5

        elif self.y_move < 0:
            self.y_move = 5
        self.y_move *= -1

