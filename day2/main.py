# Day 2 Project: Tip Calculator

class Tip_calculator:
  def __init__(self):
    self.tota_bill = None
    self.tip_amount = None
    self.split = None
    self.result = None

    print('Welcome to the tip calculator')

    self.tota_bill = int(input('What is the total amount of the bill: \n'))
    self.tip_amount = int(input('Select the tip amount between 10, 15, 20: \n'))
    self.split = int(input('Enter the number of peoople you want to split the bill with: \n'))

    self.result = (self.tota_bill * self.tip_amount / 100 + self.tota_bill) / self.split

    print(f'Each person will pay {self.result}')

Tip_calculator()
    