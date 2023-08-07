COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 300

from turtle import Turtle
from random import randint, choice

class CarManager(Turtle):
    
        def __init__(self) -> None:
            super().__init__()
            self.shape("square")
            self.penup()
            self.setheading(180)
            self.color(choice(COLORS))
            self.goto(x=START_X,y= randint(-250, 250))
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.curspeed = STARTING_MOVE_DISTANCE  
            
        def move(self, speed):
            self.forward(speed)
            
            
        
            
