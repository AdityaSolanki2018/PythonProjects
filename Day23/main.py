import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    level = scoreboard.level
    car_manager.create_car(level)  # Assuming this method exists in CarManager
    car_manager.move_cars()

    if player.ycor() > 280:
        player.reset_position()
        car_manager.car_speed += 5
        scoreboard.increase_level()  # Assuming this method exists in Scoreboard

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()  # Assuming this method exists in Scoreboard
            game_is_on = False
            print("Game Over")   
    


screen.exitonclick()