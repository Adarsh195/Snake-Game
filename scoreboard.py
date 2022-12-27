from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count=0
        self.score()

    def score(self):

        self.color("white")
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.count}", move=False, align='center', font=('Arial', 15, 'bold'))
        self.count += 1
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align='center', font=('Arial', 15, 'bold'))