from turtle import Turtle


class Snake:
    starting_position = [(0, 0), (-20, 0), (-40, 0)]
    snakes = []

    for position in starting_position:
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        snakes.append(new_snake)

    def move(self):
        for seg_num in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[seg_num - 1].xcor()
            new_y = self.snakes[seg_num - 1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.snakes[0].forward(20)
