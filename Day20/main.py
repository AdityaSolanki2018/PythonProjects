from turtle import Turtle, Screen
import time
import snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)  # Turns off the screen updates for better performance
snake_game = snake.Snake()
screen.listen()

is_game_over = False

while(not is_game_over):
    if snake_game.head.xcor() > 290 or snake_game.head.xcor() < -290 or snake_game.head.ycor() > 290 or snake_game.head.ycor() < -290:
        is_game_over = True
        print("Game Over")
    screen.update()  # Manually update the screen
    time.sleep(0.1)  # Control the speed of the game
    snake_game.move()  # Move the snake
    # Here you can add more game logic, like checking for collisions or food consumption
    screen.onkey(key="Left", fun=snake_game.left)
    screen.onkey(key="Right", fun=snake_game.right)
    screen.onkey(key="Up", fun=snake_game.up)
    screen.onkey(key="Down", fun=snake_game.down)
screen.exitonclick()