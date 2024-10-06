#making a ticket of lottery
from random import choice
#chars = [0,1,2,3,4,5,6,7,8,9,'a','e','i','o','u']

class Lottery:
    def __init__(self,numbers = 4):
        self.numbers = numbers
    
    def ticket(self, chars = [0,1,2,3,4,5,6,7,8,9,'a','e','i','o','u']):
        ticket = ''
        for i in range(self.numbers):
            i = str(choice(chars))
            ticket += i
        
        print('Any ticket matching these 4 numbers or letters wins:')
        print(f'Ticket: {ticket}')

new_try = Lottery()
ticket = new_try.ticket()