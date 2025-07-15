from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(300, random.randint(-240, 240))
        self.all_cars.append(new_car)

    def create_car(self,level):
        if level < 3:    
            if random.randint(1, 6) == 1:
                self.car()
        elif level < 6:
            if random.randint(1, 4) == 1:
                self.car()
        else:
            if random.randint(1, 3) == 1:
                self.car()


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
 
    