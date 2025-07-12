from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Snake class to manage the snake's segments and movement
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()  # Initialize the snake with its segments

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.add_segment(position)
            self.head = self.segments[0]

    def add_segment(self,position):
            t = Turtle("square")
            t.color("white")    
            t.penup()
            t.goto(position)
            self.segments.append(t)

    # Method to move the snake forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    # Methods to change the direction of the snake
    # These methods ensure the snake cannot turn back on itself
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    # Method to increase the length of the snake
    # This is called when the snake eats food
    def increase_length(self):
        self.add_segment(self.segments[-1].position())