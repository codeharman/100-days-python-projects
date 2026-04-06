# Project Password Generator

import random

letters = [
  'a','b','c','d','e','f','g','h','i','j','k','l','m',
  'n','o','p','q','r','s','t','u','v','w','x','y','z',
  'A','B','C','D','E','F','G','H','I','J','K','L','M',
  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [
  '!','@','#','$','%','^','&','*','(',')',
  '-','_','=','+','[',']','{','}','|',
  ';',':','"',"'","<",">",',','.','?','/'
]

class Password:
  def __init__(self):
    self.num_of_letters = None
    self.num_of_symbols = None
    self.num_of_numbers = None


  def generator(self):
    
    self.num_of_letters = input('How many letters do you want: \n')
    self.num_of_symbols = input('How many symbols do you want: \n')
    self.num_of_numbers = input('How many numbers do you want: \n')

    result = []

    try:
      num_to_pick = int(self.num_of_letters)
      num_of_numbers = int(self.num_of_numbers)
      num_of_symbols = int(self.num_of_symbols)
    except ValueError:
       print('please try again by putting enter number')
       return

    if (
        (num_to_pick <= len(letters)) and
        (num_of_numbers <= len(numbers)) and
        (num_of_symbols <= len(symbols))
      ):
        result.extend(random.sample(letters, num_to_pick))
        result.extend(random.sample(numbers, num_of_numbers))
        result.extend(random.sample(symbols, num_of_symbols))
    else: 
       print('please enter a valid number')
    
    random.shuffle(result)
    final_result = ''.join(result)
    print(f'Your Random Password is: {final_result}')

  
    

res = Password()
res.generator()