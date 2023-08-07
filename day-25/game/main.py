import turtle
from game import Game

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game = Game()
game_on = True
while game_on:
        userbet = screen.textinput(title="{}/50 states correct".format(game.correct), prompt="guess a state").capitalize()
        if userbet.lower() == "exit":
                game.new_file() 
                break
        else:
                game.write_up(userbet)
        if game.correct == 50:
                break


