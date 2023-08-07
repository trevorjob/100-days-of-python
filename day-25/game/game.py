import pandas
from turtle import Turtle
DATA = pandas.read_csv("50_states.csv")
FONT = ("arial", 10, "normal")
ALIGNMENT = "center"

class Game:
        def __init__(self) -> None:
                self.states = DATA["state"].to_list()
                self.x = DATA["x"].to_list()
                self.y = DATA["y"].to_list()
                self.correct = 0
                self.guessed_states = []
        
        
        def check_input(self, input):
                if input in self.states:
                        return self.states.index(input)
                else:
                        return None
        
        def write_up(self,input):
                num = self.check_input(input)
                if num is not None:
                        new_t = Turtle()
                        new_t.color("black")
                        new_t.penup()
                        new_t.hideturtle()
                        new_t.goto(y=self.y[num], x=self.x[num])
                        new_t.write("{}".format(self.states[num]),align=ALIGNMENT, font=FONT)
                        self.correct += 1
                        self.guessed_states.append(input)
        
        def new_file(self):
                dict = {
                        "states": [state for state in self.states if state not in self.guessed_states]
                }
                file = pandas.DataFrame(dict)
                file.to_csv("states_to_learn.csv")