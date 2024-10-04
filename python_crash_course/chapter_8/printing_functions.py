def send_messages(send_msg,sent_msg):
    #adding args one by one to a new list
    while send_msg:
        text = send_msg.pop()
        sent_msg.append(text)

def print_sents(sent_msg):
    #printing the args in the new list
    for sent in sent_msg:
        print(sent)
