 #Step 1 

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

random_word = random.choice(word_list)

print('Random word: ', random_word)

guess = input('Guess a letter: ')

guess = guess.lower()


index = random_word.find(guess)
indexes = []

while index >= 0:
  indexes.append(index)
  index = random_word.find(guess, index+1)


for i in range(0, len(random_word)):
  if i in indexes:
    print('Right')
  else:
    print('Wrong')
  






