# Project Hangman

import random

class Game:
  def __init__(self):
    pass

  random_word = ['hello', 'bye', 'why']
  random_num = random.choice(random_word)
  lives_left = 5
  value = input(f'guess the word: ')

  def print(self):
    for v in self.random_num:
      if self.value == v:
        print('true')
      else:
        print('false')

gg = Game()
gg.print()