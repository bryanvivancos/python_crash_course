#Comprobando la cantidad de intentos tomaría ganar la loteria
from lot import Lottery

#llamada de la clase lottery
posibilities = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e']
new_try = Lottery(4)

#my ticket
my_ticket = new_try.ticket(posibilities)

#inicio de comprobación
plays = 0

max_tries = 1_000_000 #intentos máximos

#comprobación
while (plays <= max_tries):
    #ticket ganador
    ticket = new_try.ticket(posibilities)
    
    if (ticket != my_ticket):
        plays += 1
        continue
    else:
        break

if plays <= max_tries: 
    print(f'Ticket ganador: {ticket}')
    print(f'Tu ticket: {my_ticket}')
    print(f'Necesitaste {plays} intentos')
else: 
    print(f'Intentaste {max_tries} veces sin ganar :(')
    print(f'Ticket ganador: {ticket}')
    print(f'Tu ticket: {my_ticket}')