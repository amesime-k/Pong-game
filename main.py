from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Welcome to the Pong Game")
screen.bgcolor("black")
screen.tracer(0)

turtle = Turtle()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()


screen.onkey(r_paddle.upward, "Up")
screen.onkey(r_paddle.downward, "Down")

screen.onkey(l_paddle.upward, "w")
screen.onkey(l_paddle.downward, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    print(ball.xcor())

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


#     Detect collision with the paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 340 or ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        ball.bounce_x()

#     Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

#     Detect when the L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()
