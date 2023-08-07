from turtle import Turtle
MOVEMENT = 10

class Ball(Turtle):
        def __init__(self) -> None:
                super().__init__()
                self.shape("circle")
                self.penup()
                self.shapesize(stretch_len=1, stretch_wid=1)
                self.color("red")
                self.x_m = 10
                self.y_m = 10
                self.move_speed = 0.1
                
        def move(self):
                y = self.ycor() + self.y_m
                x = self.xcor() + self.x_m
                self.goto(x=x, y=y)


        def bounce(self):
                self.y_m *= -1

        def pad_hit(self):
                self.x_m *= -1
                self.move_speed *= .9

        def reset(self):
                self.goto(0,0)
                self.move_speed = 0.1
                self.bounce()
                self.pad_hit()
        # def added(self):