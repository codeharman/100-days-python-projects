# Day 1 Project: Band Name Generator

class Name_generator:
  def __init__(self):
    self.city = None
    self.pet = None

    self.city = input('Which city do you live in?\n')
    self.pet = input("What is the name of your pet? \n")

    print(f'Your unique band name is {self.city} {self.pet} Band')

Name_generator()