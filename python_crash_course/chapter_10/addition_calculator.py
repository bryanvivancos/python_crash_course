#catch an error if input is not a number
#the user can continue entering number even if the user make a mistake and enter text instead of a number

while True: 
    try:
        num1 = int(input('Please input a first number to add: '))
        num2 = int(input('Please input a second number to add: '))
    except ValueError:
        print('Sorry, you have to enter a number')
    else:
        
        print(f'Result: {num1 + num2}')
        break