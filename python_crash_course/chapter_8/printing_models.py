#comentario
from printing_functions import *

to_send = ["archivo1", 'archivo2', 'archivo 3']
sent = []

#executing functions
send_messages(to_send[:], sent)
print('Sending messages...')
print_sents(sent)
print('... Sent')

#verifying the lists
print('\nPrinting lists...:')
print(to_send)
print(sent)