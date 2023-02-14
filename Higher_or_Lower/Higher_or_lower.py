# For debugging usage: https://pythontutor.com/
from arts import logo, vs, crying_cat
import random
from game_data import data
from replit import clear

def game_ends(current_score):
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {current_score}")
    print(crying_cat)
    play_again = input("Play again for yes press 'y' for no press 'n' ?: ")
    if play_again == 'y' or play_again == 'Y':
        game(0, None, data)

def find_index(target_name, data_list):
    for i in range(0, len(data_list)):
        item = data_list[i]
        if item['name'] == target_name:
            return i
    return -1

def game(current_score=0, current_A=None, data_center=[]):
    A = {}
    B = {}
    print(logo)
    if current_score > 0 and current_A != None:
        print('You are right! Current score is: ', current_score)
        A = current_A
    else:
        A = random.choice(data_center)

    index_a = find_index(A['name'], data_center)
    del data_center[index_a]

    B = random.choice(data_center)
    index_b = find_index(A['name'], data_center)
    del data_center[index_b]

    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

    more_followers = input("Who has more followers? Type 'A' or 'B': ")

    if A['follower_count'] > B['follower_count']: # if A has more followers
        if more_followers == 'A' or more_followers == 'a':
            current_score+=1
            data_center.append(A)
            data_center.append(B)
            game(current_score, B, data_center)
        else: 
            game_ends(current_score)
    else: #if B has more followers
        if more_followers == 'B' or more_followers == 'b':
            current_score+=1
            data_center.append(A)
            data_center.append(B)
            game(current_score, B, data_center)
        else:
            game_ends(current_score)
game(0, None, data)