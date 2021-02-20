from turtle import Turtle
FONT=("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)

    def score_up(self):
        self.level+=1
        self.update_score()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)