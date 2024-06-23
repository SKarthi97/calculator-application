from operations import *


def welcome():
    print('''
    Welcome to Calculator      
    ''')


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
            