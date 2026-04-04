# Day 3 Project: Treasure Island

class Treasure:
  def __init__(self):
    print('''
--------------------------------------------------------------------.
| .--                    FEDERAL REVERSE NOTE                    .-- |
| |_       ......    THE UNTIED STATES OF AMERICA                |_  |
| __)    ``````````             ______            B93810455B     __) |
|      2        ___            /      \                     2        |
|              /|~\\          /  _-\\  \           __ _ _ _  __      |
|             | |-< |        |  //   \  |         |_  | | | |_       |
|              \|_//         | |-  o o| |         |   | `.' |__      |
|               ~~~          | |\   b.' |                            |
|       B83910455B           |  \ '~~|  |                            |
| .--  2                      \_/ ```__/    ....            2    .-- |
| |_        ///// ///// ////   \__\'`\/      ``  //// / ////     |_  |
| __)                   F I V E  D O L L A R S                   __) |
`--------------------------------------------------------------------'
 Welcome to the Tresure Island''')
    
    choices1 = input('Youre on the island, choose right to go to the forest or left to wait at the shore \n')
    
    if choices1 == 'left':
      choices2 = input('You have arrived inside the forest, choose \wait\ to wait or \continue\ to remain on the journey \n')
      if choices2 == 'continue':
        choices3 = input('you reached to a temple it has 3 door, choose blue, yellow or green \n')
        if choices3 == 'blue':
          print('Monsters eat you up....lol')
        elif choices3 == 'yellow':
          print('snakes are waiting for you .... game over lol')
        else: 
          print('congrats you found 1 trillion crypto coins which is equilant to $1 usd')
      else:
        print('a bear came to say hi to you..... game over')
    else:
      print('bro youre here for the tressure hunt not for vacation.... game over')

Treasure()
  
  