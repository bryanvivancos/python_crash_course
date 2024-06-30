prompt = "\nPlease enter your age: "
prompt += "\n(Enter quit to finish) "

enter = ""
while enter != "quit":
    enter = input(prompt)

    if enter == "quit":
        break
    elif int(enter) < 3:
        print("Ticket is free")
    elif int(enter) < 13:
        print("Ticket is $10")
    elif int(enter) >=13:
        print("Ticket is $15")

