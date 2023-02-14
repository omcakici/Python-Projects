# For debugging usage: https://pythontutor.com/
from arts import logo, vs, crying_cat
import random
from game_data import data
from replit import clear

# Define a function to end the game
def game_ends(current_score):
    clear()
    print(logo)
    # Print the final score and ask the user if they want to play again
    print(f"Sorry, that's wrong. Final score: {current_score}")
    print(crying_cat)
    play_again = input("Play again for yes press 'y' for no press 'n' ?: ")
    # If the user wants to play again, start a new game with a score of 0
    if play_again == 'y' or play_again == 'Y':
        clear()
        game(0, None, data)

# Define a function to find the index of an item in a list of dictionaries
def find_index(target_name, data_list):
    for i in range(0, len(data_list)):
        item = data_list[i]
        if item['name'] == target_name:
            return i
    return -1

# Define the main game function
def game(current_score=0, current_A=None, data_center=[]):
    A = {}
    B = {}
    print(logo)
    # If this is not the first round and the user got the previous answer correct, keep the same A item
    if current_score > 0 and current_A != None:
        print('You are right! Current score is: ', current_score)
        A = current_A
    else:
        # Otherwise, choose a new A item at random from the data
        A = random.choice(data_center)

    # Remove the A item from the data so it won't be chosen again
    index_a = find_index(A['name'], data_center)
    del data_center[index_a]

    # Choose a B item at random from the remaining data
    B = random.choice(data_center)

    # Print the A and B items for comparison
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

    # Ask the user which item has more followers
    more_followers = input("Who has more followers? Type 'A' or 'B': ")

    # Determine whether A or B has more followers and update the score accordingly
    if A['follower_count'] > B['follower_count']: # if A has more followers
        if more_followers == 'A' or more_followers == 'a':
            current_score+=1
            data_center.append(A)
            # If the user got the answer right, start a new round with the same A item and an updated score
            game(current_score, B, data_center)
        else: 
            # If the user got the answer wrong, end the game and print the final score
            game_ends(current_score)
    else: #if B has more followers
        if more_followers == 'B' or more_followers == 'b':
            current_score+=1
            data_center.append(A)
            # If the user got the answer right, start a new round with the same A item and an updated score
            game(current_score, B, data_center)
        else:
            # If the user got the answer wrong, end the game and print the final score
            game_ends(current_score)
    
game(0, None, data)

