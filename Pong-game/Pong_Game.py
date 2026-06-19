from turtle import Screen
from Paddle import paddle
import time
from Ball import ball
from Scoreboard import Scoreboards

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=730)
screen.title("pong")
screen.tracer(0)

down_paddle = paddle((0, -340))
up_paddle = paddle((0, 350))
pong_ball = ball()
scoreboard = Scoreboards()


def close_game():
    screen.bye()

screen.listen()

screen.onkey(close_game, "Escape")

# Down paddle right
screen.onkeypress(down_paddle.start_right, "Right")
screen.onkeyrelease(down_paddle.stop_right, "Right")

# Down paddle right
screen.onkeypress(down_paddle.start_left, "Left")
screen.onkeyrelease(down_paddle.stop_left, "Left")

# Upper paddle right
screen.onkeypress(up_paddle.start_right, "d")
screen.onkeyrelease(up_paddle.stop_right, "d")

screen.onkeypress(up_paddle.start_right, "D")
screen.onkeyrelease(up_paddle.stop_right, "D")

# Upper paddle left
screen.onkeypress(up_paddle.start_left, "a")
screen.onkeyrelease(up_paddle.stop_left, "a")

screen.onkeypress(up_paddle.start_left, "A")
screen.onkeyrelease(up_paddle.stop_left, "A")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.04)

    pong_ball.ball_move()

    pong_ball.bounce_x()

    # Down paddle
    if down_paddle.move_right and down_paddle.xcor() < 235:
        new_Z = down_paddle.xcor() + 20
        down_paddle.goto(new_Z, down_paddle.ycor())

    if down_paddle.move_left and down_paddle.xcor() > -245:
        new_Z = down_paddle.xcor() - 20
        down_paddle.goto(new_Z, down_paddle.ycor())

    # Up paddle
    if up_paddle.move_right and up_paddle.xcor() < 235:
        new_x = up_paddle.xcor() + 20
        up_paddle.goto(new_x, up_paddle.ycor())

    if up_paddle.move_left and up_paddle.xcor() > -245:
        new_x = up_paddle.xcor() - 20
        up_paddle.goto(new_x, up_paddle.ycor())


    if pong_ball.ycor() > 330 and pong_ball.distance(up_paddle) < 50 or pong_ball.ycor() < -320 and pong_ball.distance(down_paddle) < 50:

        pong_ball.bounce_y()
        print("touched")

    if pong_ball.ycor() > 360:
        pong_ball.ball_out()
        scoreboard.increase_up_scoreboard()

    if pong_ball.ycor() < -360:
        pong_ball.ball_out()
        scoreboard.increase_down_scoreboard()
