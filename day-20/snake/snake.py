from turtle import Turtle

MOVE_DISTANCE = 20
DIRECTION =  (00.00, -20.00, -40.00)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
       
        def __init__(self) -> None:
                self.snake_arr = []
                self.create()
                self.head = self.snake_arr[0]
                        
                        
        def create(self):
                for _ in range(3):
                        self.tim = Turtle()
                        self.tim.color("white")
                        self.tim.penup()
                        self.tim.shape("square")
                        self.tim.color("white")
                        self.snake_arr.append(self.tim)
                        self.snake_arr[_].setx(DIRECTION[_])
                        
                        
        def move(self):                        
                for snake in range(len(self.snake_arr) - 1, 0, -1):
                        new_x = self.snake_arr[snake - 1].xcor()
                        new_y = self.snake_arr[snake - 1].ycor()
                        self.snake_arr[snake].goto(new_x,new_y)
                self.head.forward(MOVE_DISTANCE)
                
        def add_body(self):
                        self.tim = Turtle()
                        self.tim.color("white")
                        self.tim.penup()
                        self.tim.shape("square")
                        self.tim.color("pink")
                        new_x = self.snake_arr[-1].xcor()
                        new_y = self.snake_arr[-1].ycor()
                        self.snake_arr.append(self.tim)
                        self.snake_arr[-1].goto(new_x, new_y)
                        
        def reset(self):
                for i in self.snake_arr:
                        i.goto(1000, 1000)
                self.snake_arr.clear()
                self.create()
                self.head = self.snake_arr[0]
                        
        def up(self):
                if self.head.heading() != DOWN:
                        self.head.setheading(UP)
        def down(self):
                if self.head.heading() != UP:
                        self.head.setheading(DOWN)
        def right(self):
                if self.head.heading() != LEFT:
                        self.head.setheading(RIGHT)
        def left(self):
                if self.head.heading() != RIGHT:
                        self.head.setheading(LEFT)

                
                        
                