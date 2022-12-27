from turtle import Turtle

INITIAL_COORDINATE = [(0, 0), (-10, 0), (-20, 0)]
head = 10


class Snake:
    def __init__(self):
        # self.coordinates = []
        self.pab = []
        self.create_snake()
        self.head = self.pab[0]

    def create_snake(self):

        for i in INITIAL_COORDINATE:
            self.add_tail(i)

    def add_tail(self,i):
        tut = Turtle()
        tut.penup()
        tut.color("white")
        tut.shape("square")
        tut.shapesize(0.5, 0.5, 1)
        tut.goto(i)
        self.pab.append(tut)

    def extend(self):
        self.add_tail(self.pab[-1].position())
    def move(self):
        for i in range(len(self.pab) - 1, 0, -1):
            x_cor = self.pab[i - 1].xcor()
            y_cor = self.pab[i - 1].ycor()
            self.pab[i].goto(x_cor, y_cor)
        self.head.forward(head)

    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180:
            self.head.left(90)

    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.right(90)

    def right(self):
        if self.head.heading() == 90:
            self.head.right(90)
        elif self.head.heading() == 270:
            self.head.left(90)
