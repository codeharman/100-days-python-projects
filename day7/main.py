import random

random_list = ['hello', 'why', 'bye']
word = random.choice(random_list)

lives = 5
placeholder = ["_"] * len(word)

while lives > 0 and "_" in placeholder:
  print("words: ", " ".join(placeholder))
  guess = input('enter the word: ').lower()

  if guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        placeholder[i] = guess
  else:
    lives -= 1
    print('You guessed it wrong', lives)

if "_" not in placeholder:
  print('You won congrats')
else:
  print('You lose try again')