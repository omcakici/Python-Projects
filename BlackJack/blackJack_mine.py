############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

from art import logo
from replit import clear
import random

class BlackJack:
    def __init__(self, user_choices, computer_choices, cards, is_over, first_init):
        clear()
        print(logo)
        self.user_choices = user_choices
        self.computer_choices = computer_choices
        self.cards = cards
        self.is_over = is_over
        self.first_init = first_init 
    
    def reply_game(self):
        clear()
        print(logo)
        self.is_over = False
        self.first_init = True
        self.user_choices.clear()
        self.user_choices.append(random.choice(self.cards))
        self.user_choices.append(random.choice(self.cards))
        self.computer_choices.clear()
        self.computer_choices.append(random.choice(self.cards))
        self.computer_choices.append(random.choice(self.cards))
        self.play_cards()

    def final_scores(self):
        user_score = self.calculate_score(self.user_choices)
        computer_score = self.calculate_score(self.computer_choices)
        print(f"Your final cards: {self.user_choices}, final score: {user_score}")
        print(f"Computer's final cards: {self.computer_choices}, final score {computer_score}")

    def print_scores(self):
        user_score = self.calculate_score(self.user_choices)
        print(f"Your cards: {self.user_choices}, current score: {user_score}")
        print(f"Computer's first card: {self.computer_choices[0]}")

    def play_cards(self):
        user_score = self.calculate_score(self.user_choices)
        computer_score = self.calculate_score(self.computer_choices)
        self.print_scores()

        if self.first_init == True:
            if self.CHECK_IS_ACE_PLUS_TEN(self.user_choices) == True or self.CHECK_IS_ACE_PLUS_TEN(self.computer_choices) == True:
                clear()
                self.final_scores()
                print('You Win! BlackJack!!')
                #Game finished in a sense
                self.is_over = True

                #At the end ask user if wheter they want to play again!
                if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
                    self.reply_game()
                else:
                    return

        # after first initialization of cards          
        self.first_init = False
        if user_score >= 21:
            self.game_finished(user_score, computer_score)
        
        else:    
            if self.is_over == False:
                if input("Type 'y' to get another card, type 'n' to pass: 'y'") == 'y':
                    self.user_choices.append(random.choice(self.cards))
                    self.computer_choices.append(random.choice(self.cards))
                    self.computer_decision()
                    self.play_cards()
                else:
                    self.computer_decision()
                    self.final_scores()
                    self.game_finished(user_score, computer_score)
            else: 
                self.final_scores()
                self.game_finished(user_score, computer_score)
      
    def game_finished(self, user_score, computer_score):
        if user_score > 21:
            print("You went over. You lose 😭")
        elif (user_score == computer_score):
            print("Draw 🙃")
        elif user_score > 21:
            print("You went over. You lose 😭")
        elif computer_score > 21:
            print("Opponent went over. You win 😁")
        elif user_score > computer_score:
            print("You win 😃")
        else:
            print("You lose 😤")
        
        #Game finished in a sense
        self.is_over = True

        #At the end ask user if wheter they want to play again!
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
            self.reply_game()

    def computer_decision(self):
      decisions = ['y', 'n']
      decide_to_play = random.choice(decisions)
      if decide_to_play == 'y':
        # add card to the computer_choices deck
        computer_choice.append(random.choice(self.cards))
      
    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.
    def calculate_score(self,cards):
        """Take a list of cards and return the score calculated from the cards"""

        #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
      
    # Check if its BlackJack
    def CHECK_IS_ACE_PLUS_TEN(self, values) -> bool:
      check_ACE = False
      check_plus_ten = False
      for c in values:
        if c == 11:
          check_ACE = True
        elif c == 10:
          check_plus_ten = True
      return check_ACE and check_plus_ten
              
if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_choice = list()
    user_choice.append(random.choice(cards))
    user_choice.append(random.choice(cards))
    computer_choice = list()
    computer_choice.append(random.choice(cards))
    computer_choice.append(random.choice(cards))
    Game = BlackJack(user_choice, computer_choice, cards, False, True).play_cards()

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
