from turtle import Turtle
FONT = ("arial", 24, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
        def __init__(self) -> None:
                super().__init__()
                self.score = 0
                self.read_file()
                self.color("white")
                self.penup()
                self.goto(00.00, 260.00)
                self.shapesize(stretch_len=2, stretch_wid=4)
                self.update_scoreboard()
                self.hideturtle()
                
        def read_file(self):
                with open("highscore.txt", "r") as file:
                        self.high_score = int(file.read())
                        
        def write_file(self):
                if self.score > self.high_score:
                        with open("highscore.txt", "w") as file:
                                file.write(str(self.score))
                
        def update_scoreboard(self):
                self.clear()
                self.write(f"score: {self.score} highscore: {self.high_score}", align=ALIGNMENT, font=FONT)
                
        def update_score(self):                
                self.score += 1
                self.update_scoreboard()
                
        def reset(self):
                self.write_file()
                self.read_file()
                self.score = 0
                self.update_scoreboard()

                
                