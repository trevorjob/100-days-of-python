from turtle import Turtle as t, Screen as s
import random

tim = t()
screen = s()

tim.shape("turtle")



# import colorgram

# color = colorgram.extract("download.jpeg", 30)
# rgb_cl = []
# for col in color:
#         r = col.rgb.r
#         g = col.rgb.g
#         b = col.rgb.b
        
#         rgb_cl.append((r,g,b))
# print(rgb_cl)

color_list = [(144, 167, 187), (190, 143, 153), (200, 155, 126), (23, 34, 48), (67, 105, 131), (150, 176, 164), (137, 71, 79), (226, 212, 122), (136, 78, 69), (132, 29, 38), (46, 29, 36), (221, 174, 181), (67, 106, 93), (182, 97, 107), (29, 49, 44), (185, 97, 89), (54, 41, 35), (24, 89, 68), (180, 189, 209), (228, 174, 167), (121, 38, 33), (172, 201, 189), (114, 124, 150), (38, 64, 95), (158, 206, 216), (73, 148, 169)] 


tim.pensize(10)
tim.speed("fastest")
sat = 0
tim.penup()

tim.setheading(220)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()

for i in range(10):        
        for _ in range(10):
                col =  random.choice(color_list)
                tim.dot(20, random.random(), random.random(), random.random())
                tim.penup()
                tim.forward(50)
                tim.pencolor('red')
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(50 * 10)
        tim.setheading(0)

        










screen.exitonclick()