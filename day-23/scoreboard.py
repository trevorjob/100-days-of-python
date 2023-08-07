FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
        def __init__(self) -> None:
                super().__init__()
                self.score = 0
                self.color("black")
                self.penup()
                self.goto(-180.00, 260.00)
                self.shapesize(stretch_len=2, stretch_wid=4)
                self.hideturtle()
                self.update_scoreboard()
        
        def update_score(self):
            self.clear()
            self.score += 1
            self.update_scoreboard()
            
        def update_scoreboard(self):
            self.write(f"turtle: {self.score}", align="center", font=FONT)
            
        def game_over(self):
                self.goto(0,0)
                self.write(f"GAME OVER", align="center", font=FONT)
