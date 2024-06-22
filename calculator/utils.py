from operations import *


operations = {'+': addition,
              '-': subtraction,
              '*': multiplication,
              '/': division,
              '**': power,
              '%': modulus,
              'abs': absolute,
              'inv': inverse}


def welcome():
    print('''
    Welcome to Calculator      
    ''')


def enter_valid_operation_input():
    # Constructing the prompt string
    prompt = "Please type in the math operation you would like to complete:\n"
    
    for symbol, operation in operations.items():
        prompt += f"    {symbol} for {operation.__name__}\n"

    operation = input(prompt)
    
    if operation in operations:
        if operation == 'abs':
            number = enter_valid_number_input("Enter your number: ")
            return operations[operation](number)
        elif operation == 'inv':
            try:
                number = enter_valid_number_input("Enter your number: ")
                return operations[operation](number)
            except ZeroDivisionError as e:
                return f"Error: {e}"
        else:
            try:
                number_1 = enter_valid_number_input('Enter your first number: ')
                number_2 = enter_valid_number_input('Enter your second number: ')
                return operations[operation](number_1, number_2)
            except ZeroDivisionError:
                return f"Error: {operations[operation].__name__} by zero"
    else:
        return f"Error: {operation} is not a valid operation"


def enter_valid_number_input(prompt):
    while True:
        value = input(prompt)
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            print('Invalid number. Please enter a valid integer or float.')
            