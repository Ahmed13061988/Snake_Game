from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    new_snake = Turtle("square")
    new_snake.color("white")
    new_snake.goto(position)

screen.exitonclick()
