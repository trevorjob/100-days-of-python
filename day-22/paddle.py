from turtle import Turtle
MOVEMENT = 20

class Paddle(Turtle):
        
        def __init__(self, x_pos) -> None:                
                self.create(x_pos)
                
        def create(self, x_pos):
                super().__init__()
                self.shape("square")
                self.color("white")
                self.penup()
                self.speed("fastest")
                self.goto(x=x_pos, y=0)
                self.shapesize(stretch_wid=5, stretch_len=1)
                
        def up(self):        
                y = self.ycor() + MOVEMENT
                self.goto(x=self.xcor(), y=y)
        
        def down(self):
                y = self.ycor() - MOVEMENT
                self.goto(x=self.xcor(), y=y)