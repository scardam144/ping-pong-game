from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)
r_p = Paddle((350, 0))
l_p = Paddle((-350, 0))
b = Ball((0, 0))

screen.listen()
screen.onkey(r_p.go_up, "Up")
screen.onkey(r_p.go_down, "Down")
screen.onkey(l_p.go_up, "w")
screen.onkey(l_p.go_down, "s")
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(b.move_speed)
    screen.update()
    b.move()
    # detect collision with wall
    if b.ycor() > 290 or b.ycor() < -290:
        b.bounce_y()
    # detect collision with paddle
    if b.distance(r_p) < 50 and b.xcor() > 320 or b.distance(l_p) < 50 and b.xcor() < -320:
        b.bounce_x()

    # further movement of ball
    if b.xcor() > 400:
        b.reset_position()
        score.l_point()

    if b.xcor() < -400:
        b.reset_position()
        score.r_point()


screen.exitonclick()
