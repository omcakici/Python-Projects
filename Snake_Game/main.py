from turtle import Turtle, Screen
import random

class SnakeGame:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 600, 600
        self.positions = [(0,0), (-20,0), (-40,0)]
        self.head = (0, 0)
        self.apple = self.generate_apple()
        self.food = (-350, 0)
        self.segments = []
        self.is_game_on = True

        for x_pos in self.positions:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(x_pos)
            snake.pendown()
            self.segments.append(snake)

    def generate_apple(self):
        x = random.randint(-self.WIDTH/2, self.WIDTH/2)
        y = random.randint(-self.HEIGHT/2, self.HEIGHT/2)
        food = Turtle("square")
        food.hideturtle()
        food.color("red")
        food.penup()
        food.setpos(x, y)
        food.showturtle()
        food.pendown()
        self.food = (x, y)

    def check_boarders(self):
        print("I will check if its going to crash the board of the grid")

    def game_engine(self):
        while self.is_game_on:
            for snake in self.segments:
                snake.penup()
                snake.forward(20)
                self.head = self.segments[0]
                snake.pendown()

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black") #changing the background color
screen.title("My Snake Game")

main = SnakeGame()
main.game_engine()

screen.exitonclick()





# print('--------------')
# print("X cord: ", snake.xcor(), " Y cord: ", snake.ycor())