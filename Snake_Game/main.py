from turtle import Turtle, Screen


class Main:
    def __init__(self):
        self.positions = [0, -20, -40]
        self.snakes = []
        self.is_game_on = True

    def init_positions(self):
        for x_pos in self.positions:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.setpos(x_pos, 0)
            snake.pendown()
            self.snakes.append(snake)

    def game_engine(self):
        counter = 1
        while self.is_game_on and counter < 10:
            for snake in self.snakes:
                snake.penup()
                new_x = snake.xcor() + 20
                snake.goto(new_x, snake.ycor())
                snake.pendown()
            
            counter += 1

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black") #changing the background color
screen.title("My Snake Game")

main = Main()
main.init_positions()
main.game_engine()

screen.exitonclick()





# print('--------------')
# print("X cord: ", snake.xcor(), " Y cord: ", snake.ycor())