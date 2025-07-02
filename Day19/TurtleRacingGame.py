from turtle import Turtle, Screen
import random
# Turtle Racing Game
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Racing Game")

# Create turtles with different colors and positions
y_positions = [-70,-40,-10,20,50]
colors = ["red", "blue", "green", "yellow", "purple"]
all_turtles = []
is_race_on = False

# Function to create a turtle with a specific color and y position
def create_turtle(color, y_position):
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(-230, y_position)
    return t

# Create turtles and add them to the all_turtles list
for i in colors:
    all_turtles.append(create_turtle(i, y_positions[colors.index(i)]))

# Ask user for their bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
if user_bet:
    is_race_on = True

# Start the
while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                screen.textinput(title="You won!", prompt=f"The {winning_color} turtle won! Press Enter to exit.")
            else:
                screen.textinput(title="You lost!", prompt=f"The {winning_color} turtle won! Press Enter to exit.")        

        # Move the turtle forward by a random distance
        random_distance = random.randint(0, 10)
        t.forward(random_distance)

screen.exitonclick()