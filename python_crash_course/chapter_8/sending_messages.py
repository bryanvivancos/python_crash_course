send = ["Hola", "Python"]
sents = [] 

def send_messages(send_msg,sent_msg):
    while send_msg:
        text = send_msg.pop()
        print(text)
        sent_msg.append(text)

        
send_messages(send,sents)

print("\nPrinting lists:")
print(f'Enviados: {send}')
print(f'Recibidos: {sents}')