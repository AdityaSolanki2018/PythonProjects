from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)  # Higher-order function: onkey takes a function as an argument
screen.exitonclick()
