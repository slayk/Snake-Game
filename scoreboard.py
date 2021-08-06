from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 16, "normal"))

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()

    def gameOver(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!\nScore: {self.score}", align="center", font=("Courier", 16, "normal"))