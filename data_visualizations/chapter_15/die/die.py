from random import randint

class Die:
    #class to define a die
    def __init__(self,num_sides = 6):
        self.num_sides = num_sides
        
    #method to roll a die
    def roll(self):
        num = randint(1,self.num_sides)
        return num
    