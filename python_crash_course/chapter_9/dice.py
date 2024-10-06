#making a code that roll a die
from random import randint
#creating Die class
class Die: 
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self):
        num = randint(1, self.sides)
        return num

#Rolling 10 times a 6-sided die
print('\nRolling 10 times a 6-sided die')
die = Die()
for roll in range(10):
    roll = die.roll_die()
    print(roll)

#Rolling 10 times a 10-sided die
print('\nRolling 10 times a 10-sided die')
die = Die(10)
for roll in range(10):
    roll = die.roll_die()
    print(roll)

#Rolling 10 times a 20-sided die
print('\nRolling 10 times a 20-sided die')
die = Die(20)
for roll in range(10):
    roll = die.roll_die()
    print(roll)