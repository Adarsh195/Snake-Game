from snake import Snake
import time
from scoreboard import Scoreboard
from turtle import Turtle,Screen
from food import Food
s=Screen()
s.setup(width=600,height=600)
s.title("Snake...sssss")
s.bgcolor("black")
s.tracer(0)
score_count=Scoreboard()
snake=Snake()
food=Food()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")
is_true=True
while is_true:
    s.update()
    time.sleep(0.1)
    snake.move()
    #Collision Detection


    if snake.head.distance(food)<7:
        food.refresh()
        score_count.score()
        snake.extend()
    #Collision with Wall

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_true=False
    #detect collision with tail
    for node in snake.pab[1:]:
        if snake.head.distance(node)<5:
            is_true = False
score_count.game_over()


s.exitonclick()