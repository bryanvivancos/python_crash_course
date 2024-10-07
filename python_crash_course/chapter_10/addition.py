#catch an error if input is not a number
try:
    num1 = int(input('Please input a first number: '))
    num2 = int(input('Please input a second number: '))
except ValueError:
    print('Sorry, you have to enter a number')
else:
    
    print(f'Result: {num1 + num2}')