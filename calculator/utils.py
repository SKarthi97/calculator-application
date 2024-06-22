from operations import *


def welcome():
    print('''
    Welcome to Calculator      
    ''')


def enter_valid_operation_input():
    operations = ['+', '-', '*', '/']
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    if operation in operations:
        return operation
    else:
        print('You have not typed a valid operator, please run the program again.')
        return enter_valid_operation_input()


def enter_valid_number_input(string_word):
    try:
        return int(input(string_word))
    except ValueError:
        print('Invalid number')
        return enter_valid_number_input(string_word)


def perform_operation(operation, number_1, number_2):
    if operation == '+':
        addition(number_1, number_2)
    elif operation == '-':
        subtraction(number_1, number_2)
    elif operation == '*':
        multiplication(number_1, number_2)
    elif operation == '/':
        division(number_1, number_2)
