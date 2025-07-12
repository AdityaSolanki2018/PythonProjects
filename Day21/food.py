from turtle import Turtle
import random 

# Food class to create food for the snake game
# Inherits from Turtle to utilize turtle graphics features
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)   # Set the size of the food
        self.speed("fastest")
        # Place the food at a random position within the game boundaries
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y) 
