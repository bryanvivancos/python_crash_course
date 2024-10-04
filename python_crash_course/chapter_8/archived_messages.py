send = ["Hola", "Python"]
sents = [] 

def send_messages(send_msg,sent_msg):
    while send_msg:
        text = send_msg.pop()
        sent_msg.append(text)

def print_sents(sent_msg):
    for sent in sent_msg:
        print(sent)

send_messages(send[:],sents)
print_sents(sents)

print("\nPrinting lists:")
print(f'Enviados: {send}')
print(f'Recibidos: {sents}')