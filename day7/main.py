# Project Hangman

import random

lists = ['hello', 'bye', 'why']
word = random.choice(lists)

lives = 5
placeholder = ['_'] * len(word)

while lives > 0 and '_' in placeholder:
  print("Words: ", ' '.join(placeholder))
  guess = input('guess the word: ').lower()
  
  if guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        placeholder[i] = guess
  else:
    lives -= 1
    print('Wrong Answer, Lives left: ', lives)

if '_' not in placeholder:
  print("Congrats you win")
else:
  print('better luck next time')