


# So this is number guessing game, you start the game with easy or hard mode depends on what you choose. 
# Computer randomly choose a number, then you start guessing which number would it be

import random
from replit import clear
from art import logo

print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")

game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

computer_number = random.randint(0, 100)

def make_guess(guess_left):
    while guess_left != 0:
        print(f"You have {guess_left} attempts remaining to guess the number.")
        user_guessed = int(input("Make a guess: "))
        if user_guessed < computer_number:
            print("Too low. \nGuess again.")
        elif user_guessed == computer_number:
            print(f"You got it! The answer was {computer_number}.")
            return True
        else:
            print("Too high. \nGuess again.")
        guess_left -= 1
    return False

if game_mode == 'easy':
    # You have 10 chances to guess the number, its easy level broer :)
    guess_left = 10
    
    if not make_guess(guess_left):
        print("You've run out of guesses, you lose.")
        print(f"The answer was: {computer_number}")

elif game_mode == 'hard':
    # its hard level so you have only 5 chances to guess the number
    guess_left = 5
    
    if not make_guess(guess_left):
        print("You've run out of guesses, you lose.")
        print(f"The answer was: {computer_number}")
    
else:
    print("!!Typed wrongly try again!!!")

