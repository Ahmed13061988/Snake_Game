from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]

snakes = []
game_is_on = True

for position in starting_position:
    new_snake = Turtle("square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(position)
    snakes.append(new_snake)

while game_is_on:
    screen.update()
    time.sleep(0.5)
    for seg_num in range(len(snakes)-1, 0, -1):
        new_x = snakes[seg_num - 1].xcor()
        new_y = snakes[seg_num - 1].ycor()
        snakes[seg_num].goto(new_x, new_y)
    snakes[0].forward(20)
screen.exitonclick()
