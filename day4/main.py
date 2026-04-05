# Project: Rock Paper Scissors

import random

class Game:
  def __init__(self):
    self.user_score = 0
    self.computer_score = 0
    self.games_left = 5

  def play(self):
    while True:
      if self.games_left == 0:
        self.winner()
        break

      user_choice = input('Choose rock, paper, scissors: \n').lower()
      computer_choice = random.choice(['rock', 'paper', 'scissors'])
      print(f'Computer chooses: {computer_choice}')

      if user_choice == computer_choice:
        print('It\'s a draw')
        self.games_left -= 1
        print(f'games left: {self.games_left}')
      elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or 
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
      ):
        self.games_left -= 1
        self.user_score += 1
        print(f'User wins {self.user_score}')
        print(f'games left: {self.games_left}')
      else:
        self.games_left -= 1
        self.computer_score += 1
        print(f'Computer wins {self.computer_score}')
        print(f'games left: {self.games_left}')
      
  def winner(self):
    if self.games_left == 0:
      if self.user_score > self.computer_score:
        print('User wins the game')
      else:
        print('Computer wins the game')


game = Game()
game.play()
    