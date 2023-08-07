# from turtle import Turtle, Screen
# timmy = Turtle()

# timmy.shape("turtle")
# print(timmy)
# timmy.color("green")
# a = 0
# while a != 7:
#         timmy.forward(50)
#         timmy.left(45)
#         a +=1
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(100)
# timmy.forward(100)
# timmy.left(100)\
        
        



# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["pikachu", "squirtle", "charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
