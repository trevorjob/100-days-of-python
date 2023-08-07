from turtle import Turtle
FONT = ("arial", 24, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
        def __init__(self) -> None:
                super().__init__()
                self.score = 0
                self.color("white")
                self.penup()
                self.goto(00.00, 260.00)
                self.shapesize(stretch_len=2, stretch_wid=4)
                self.update_scoreboard(0,0)
                self.hideturtle()
                
        def update_scoreboard(self, rscore, lscore):
                self.write(f"{rscore} : {lscore}", align=ALIGNMENT, font=FONT)
        
        def update_score(self, rscore, lscore):
                self.clear()
                self.score += 1
                self.update_scoreboard(rscore, lscore)