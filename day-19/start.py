from turtle import Turtle, Screen
import random

# tim = Turtle()
# max = Turtle()
screen = Screen()

# def move_forward():
#         tim.forward(10)
#         max.forward(10)
# def move_backward():
#         tim.backward(10)
#         max.backward(10)
# def turn_l():
#         tim.left(10)
# def turn_r():
#         tim.right(10)
# def clear():
#         tim.reset()

screen.setup(width=500, height=400)

# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="a", fun=turn_l)
# screen.onkey(key="d", fun=turn_r)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="c", fun=clear)

colors = ["red", "green", "blue", "pink", "purple",]
is_race_on = False
b = -100
userbet = screen.textinput(title="make a bet", prompt="which turtle will win the race")
all_turtles = []
for _ in range(5):
        tim = Turtle(shape="turtle")
        tim.penup()
        tim.color(colors[_])
        tim.goto(x=-220, y=b)
        all_turtles.append(tim)
        
        b += 30
        
if userbet:
        is_race_on = True

while is_race_on:
        for i in all_turtles:
                ra = random.randint(0,10)
                i.forward(ra)
                if i.xcor() >= float(230): break
                
        if i.xcor() >= float(230):
                if userbet.lower() == i.color()[0]:
                        print(f"you won {i.color()[0]} won the race")
                else :
                        print(f"you loose {i.color()[0]} won the race")
                break

screen.exitonclick()