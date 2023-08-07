from turtle import Turtle
import random
class Food(Turtle):
        def __init__(self) -> None:
                super().__init__()
                self.shape("circle")
                self.penup()
                self.shapesize(stretch_len=0.5, stretch_wid=0.5)
                self.color("red")
                self.speed("fastest")
                self.refresh()
                
        def refresh(self):
                ran_x =  random.randint(-270, 270)
                ran_y =  random.randint(-270, 270)
                self.goto(ran_y,ran_x)