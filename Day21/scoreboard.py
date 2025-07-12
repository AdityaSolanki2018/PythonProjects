from turtle import Turtle

# Constants for scoreboard alignment and font
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Scoreboard class to manage the score display
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    # Method to update the scoreboard display
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Method to display game over message
    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
