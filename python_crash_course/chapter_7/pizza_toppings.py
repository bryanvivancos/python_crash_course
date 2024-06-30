prompt = "\nEnter your topping:"
prompt += "\n(Enter quit to finish) "

topping= ""

while topping != "quit":    
    topping = input(prompt)
    
    if topping != "quit":
        print(f"You just add {topping.title()} to your pizza")