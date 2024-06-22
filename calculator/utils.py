from operations import *

operations = {'+': 'addition',
              '-': 'subtraction',
              '*': 'multiplication',
              '/': 'division',
              '**': 'power',
              '%': 'modulo'}


def welcome():
    print('''
    Welcome to Calculator      
    ''')


def enter_valid_operation_input():
    # Constructing the prompt string
    prompt = "Please type in the math operation you would like to complete:\n"

    for symbol, operation in operations.items():
        prompt += f"    {symbol} for {operation}\n"

    operation = input(prompt)
    if operation in operations:
        return operation
    else:
        print('You have not typed a valid operator, please run the program again.')
        return enter_valid_operation_input()


def enter_valid_number_input(string_word):
    try:
        value = input(string_word)
        if '.' in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        print('Invalid number. Please try again.')
        return enter_valid_number_input(string_word)


def perform_operation(operation, number_1, number_2):
    if operation == '+':
        addition(number_1, number_2)
    elif operation == '-':
        subtraction(number_1, number_2)
    elif operation == '*':
        multiplication(number_1, number_2)
    elif operation == '/':
        try:
            division(number_1, number_2)
        except ZeroDivisionError:
            print("Division by zero")
    elif operation == '**':
        power(number_1, number_2)
    elif operation == '%':
        try:
            modulus(number_1, number_2)
        except ZeroDivisionError:
            print("Modulo by zero")
