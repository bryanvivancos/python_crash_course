#Comprobando la cantidad de intentos tomaría ganar la loteria
from lot import Lottery

#llamada de la clase lottery
new_try = Lottery()

#ticket ganador
ticket = new_try.ticket()

#my ticket
my_ticket = new_try.ticket()

#inicio de comprobación
plays = 0

max_tries = 1_000_000 #intentos máximos

#comprobación
while (plays <= max_tries):
    new_try = Lottery()
    ticket = new_try.ticket()
    
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