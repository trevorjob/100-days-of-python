from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
score = Scoreboard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game = True
while game:
        screen.update()
        time.sleep(.1)
        snake.move()
        
        if snake.head.distance(food) < 15:
                food.refresh()
                snake.add_body()
                score.update_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
                score.reset()
                snake.reset()
        
        for sn in snake.snake_arr[1:]:
                if snake.head.distance(sn) < 10:
                        score.reset()   
                        snake.reset()           
      
                




screen.exitonclick()