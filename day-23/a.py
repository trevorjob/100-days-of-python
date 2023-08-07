# import time
from turtle import Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard
# import threading
# import random

screen = Screen()
screen.setup(width=600, height=600)
# screen.tracer(0)

# player = Player()
# car_arr = []

# def car_create():
#     i = 10
#     while i:
#         car = CarManager()
#         time.sleep(random.randint(1, 4))
#         car_arr.append(car)
#         i-=1
        


# screen.listen()
# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.onkey(player.move, "Up")
    # class_thread = threading.Thread(target=car_create)
    # for i in car_arr:
    #     i.move()
    #     if player.distance(i) < 18:
    #         game_is_on = False
    
    # screen.update()


screen.exitonclick()