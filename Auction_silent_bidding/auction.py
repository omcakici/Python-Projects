from replit import clear
from art import logo
import sys
#HINT: You can call clear() to clear the output in the console.

auction_dict = {}

print(logo)
print("Welcome to the secret auction program.")

is_any_other_bidder = True

while is_any_other_bidder:
  name = input("What's your name?: ")
  bid = int(input("What's your bid?: $"))
  auction_dict[name] = bid
  any_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
  if any_bidder == 'no':
    is_any_other_bidder = False
  elif any_bidder == 'yes':
    is_any_other_bidder = True
    clear()
  else: 
    print("Type only 'yes' or 'no'")
    is_any_other_bidder = False

is_it_draw = False
find_max_bid = -sys.maxsize-1
find_winner = ''
for key, value in auction_dict.items():
  if value > find_max_bid:
    find_max_bid = value
    find_winner = key
  elif value == find_max_bid:
    is_it_draw = True

if not is_it_draw:
  print(f"The winner is {find_winner} a bid of ${auction_dict[find_winner]}.")
else:
  print('It is a draw')



