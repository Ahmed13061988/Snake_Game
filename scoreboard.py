from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def updating_scoreboard(self):
        self.write(f"Score: {self.score} ", align="center", font=('Arial', 20, 'normal'))

    def scoring(self):
        self.score += 1
        self.clear()
        self.updating_scoreboard()

    def game_over(self):
        self.clear()
        self.write(f"Game Over!", align="center", font=('Arial', 20, 'normal'))
