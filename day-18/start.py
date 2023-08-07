from turtle import Turtle as t, Screen as s
import random

tim = t()
screen = s()

tim.shape("turtle")
tim.color('pink', 'green')
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# for i in range(40):
#         tim.penup()
#         tim.forward(5)
#         tim.pendown()
#         tim.forward(5)
        
        
# for i in range(3,10):
#         tim.pensize(10)
#         for a in range(i):
#                 a = tim.forward
#                 num = 360 / i
#                 a(75)
#                 tim.right(num)

#         tim.pencolor(random.random(), random.random(), random.random())

# pick = [tim.forward, tim.backward]
# direction = [tim.right, tim.left]
# dir = [0, 90, 180, 270]
# tim.pensize(5)
tim.speed("fastest")
# for i in range(2000):
#         picked = random.choice(pick)
#         # d = random.choice(direction)
#         tim.pencolor(random.random(), random.random(), random.random())
#         picked(25)
#         tim.setheading(random.choice(dir))

# for i in range(50):
#         tim.circle(50)
#         tim.left(15)
#         tim.pencolor(random.random(), random.random(), random.random())


while True:
        tim.circle(50)
        tim.setheading(tim.heading() + 3)
        tim.pencolor(random.random(), random.random(), random.random())

        if (tim.heading() == 0.0):
                break

screen.exitonclick()