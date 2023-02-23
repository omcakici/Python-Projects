# importing necessary modules
from turtle import Turtle, Screen
import random

# main class
class Main:
    # initializing class attributes
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=500, height=400)
        self.user_guessed_winner = self.screen.textinput(title="Turtle Game", prompt="Which turtle will win pick one of them:(red/green/blue/purple/yellow/black/brown)? ")
        self.turtle_colors = ["red", "green", "blue", "purple", "yellow", "black", "brown"]
        self.y_positions = [-150, -100, -50, 0, 50, 100, 150]

    # checking the user's guess
    def check_guess(self):
        if self.user_guessed_winner != "red" and self.user_guessed_winner != "green" and self.user_guessed_winner != "blue"  and self.user_guessed_winner != "purple" and self.user_guessed_winner != "yellow" and  self.user_guessed_winner != "black" and self.user_guessed_winner != "brown":
            self.screen.bye()
    
    # initializing turtles
    def init_turtles(self):
        # lift up the pen
        for index in range(0, 7):
            turtle = Turtle("turtle")
            turtle.penup()
            turtle.color(self.turtle_colors[index])

            # move the turtle to the desired position
            turtle.goto(-230, self.y_positions[index])
            # put the pen back down
            turtle.pendown()

    # giving random speeds to turtles
    def give_random_speeds(self, turtle):
        turtle.penup()
        turtle.forward(random.randint(0, 20))
        turtle.pendown()

    # checking if the game has ended
    def is_game_ended(self, turtle):
        if turtle.xcor() > self.screen.window_width()/2-40:
            return True
        return False

    # running the game engine
    def game_engine(self, game_goes_on):
        while game_goes_on == True:
            for turt in self.screen.turtles():
                self.give_random_speeds(turt)
                if self.is_game_ended(turt): 
                    winner_message = "The winner is " + turt.pencolor() + "!"
                    turt.write(winner_message, font=("Arial", 16, "bold"), align="center")
                    if turt.pencolor() != self.user_guessed_winner:
                        # find the green turtle
                        assumed_winner = next((t for t in self.screen.turtles() if t.pencolor() == self.user_guessed_winner), None)
                        assumed_winner.write("Looser that you picked!", font=("Arial", 16, "bold"), align="center")
                        game_goes_on = False
                        break

# instantiating Main class
main = Main()
# initializing turtles
main.init_turtles()
# running the game engine
main.game_engine(True)
# keeping the screen open
main.screen.mainloop()