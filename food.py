from turtle import Turtle
import random as r
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.3, 0.3, 1)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        ran_x = r.randint(-280, 280)
        ran_y = r.randint(-280, 280)
        self.goto(ran_x, ran_y)


