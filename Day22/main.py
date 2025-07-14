from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

#  Set up screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turns off the screen updates for better performance

score = ScoreBoard()  # Initialize the scoreboard
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")  # Move left paddle up with 'w'
screen.onkey(l_paddle.go_down, "s")  # Move left paddle down with    
screen.onkey(r_paddle.go_up, "Up")  # Move right paddle up with 'Up'
screen.onkey(r_paddle.go_down, "Down")  # Move right paddle down with 'Down'


game_is_on = True
while(game_is_on):
    screen.update()  # Update the screen to reflect changes
    time.sleep(0.07)  # Control the speed of the game
    # Add game logic here, such as paddle movement and ball collision
    ball.move()  # Move the ball

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() == 340 and ball.distance(r_paddle) < 50 or ball.xcor() == -340 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380 :
        score.l_point()  # Left paddle scores
        ball.reset()  # Reset the ball if it goes out of bounds

    if ball.xcor() < -380:
        score.r_point()
        ball.reset()

    if score.l_score == 5 or score.r_score == 5:
        game_is_on = False
        score.clear()
        score.goto(0, 0)
        score.color("red")
        score.write("Game Over", align="center", font=("Courier", 24, "normal"))
    
screen.exitonclick()  # Exit on click