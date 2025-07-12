from turtle import Turtle, Screen
import time
import snake
from food import Food 
import random
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates for better performance

# Initialize the snake, food, and scoreboard
scoreboard = Scoreboard()
snake_game = snake.Snake()
food = Food()

# Set up the keyboard bindings
screen.listen()
screen.onkey(key="Left", fun=snake_game.left)
screen.onkey(key="Right", fun=snake_game.right)
screen.onkey(key="Up", fun=snake_game.up)
screen.onkey(key="Down", fun=snake_game.down)

# Initialize the game state
is_game_over = False

# Main game loop
while(not is_game_over):
    screen.update()  # Manually update the screen
    time.sleep(0.1)  # Control the speed of the game
    snake_game.move()  # Move the snake

    # Check for boundary collisions
    if snake_game.head.xcor() > 290 or snake_game.head.xcor() < -290 or snake_game.head.ycor() > 290 or snake_game.head.ycor() < -290:
        is_game_over = True
        scoreboard.game_over()
        
    # Detect collision with food
    if snake_game.head.distance(food) < 15:  # Assuming food is a Turtle object
        food.goto(random.randint(-280, 280), random.randint(-280, 280))  # Move food to a new random position
        # Increase the length of the snake when it eats food
        snake_game.increase_length()  
        # Increase the score
        scoreboard.score += 1
        # Update the scoreboard
        scoreboard.update_scoreboard()  

    # Check for self-collision 
    for segment in snake_game.segments[1:]:
        if snake_game.head.distance(segment) < 10:
            is_game_over = True
            scoreboard.game_over()

# Finalize the game
screen.exitonclick()