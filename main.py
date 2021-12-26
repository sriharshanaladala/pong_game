from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong game")

screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
