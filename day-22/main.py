from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

MOVEMENT = 20

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)
scoreboard = Scoreboard()

r_pad = Paddle(350)
l_pad = Paddle(-350)
ball = Ball()
screen.listen()


screen.onkey(r_pad.up,"Up")
screen.onkey(r_pad.down, "Down")
screen.onkey(l_pad.up,"w")
screen.onkey(l_pad.down, "s")

game = True
rscore = 0
lscore = 0

while game:
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce()
                
        if (ball.distance(r_pad) < 50 and ball.xcor() > 330) or (ball.distance(l_pad) < 50 and ball.xcor() < -330)  :
                ball.pad_hit()
        
        if ball.xcor() > 360:
                rscore+=1
                ball.reset()
                
        elif ball.xcor() < -360:
                lscore+=1
                ball.reset()
        scoreboard.update_score(rscore,lscore)
        time.sleep(ball.move_speed)
        



screen.exitonclick()