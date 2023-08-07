import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5
speed = STARTING_MOVE_DISTANCE
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_arr = []

screen.listen()
game_is_on = True
count = 0
lvl = False
while game_is_on:
    time.sleep(0.1)
    screen.onkey(player.move, "Up")
    
    if count % 6 == 0:
        car = CarManager()
        
        car_arr.append(car)

    for i in car_arr:
        i.move(speed)
        if player.distance(i) < 20:
            scoreboard.game_over()
            game_is_on = False
    count+= 1
    
    if player.ycor() >= 280:
        scoreboard.update_score()
        
        player.pPosition()
        count = 0          
        speed += MOVE_INCREMENT  
            
    screen.update()


screen.exitonclick()