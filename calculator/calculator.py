from utils import *

        
# Define calculate function
def calculate():
    operation = enter_valid_operation_input()
    number_1 = enter_valid_number_input('Enter your first number: ')
    number_2 = enter_valid_number_input('Enter your second number: ')

    # Add a perform operation function to calculate the output
    perform_operation(operation, number_1, number_2)
    
    # Add repeat function to calculate() function
    repeat_again()


# Define a repeat_again function to call the calculate function repeatedly
def repeat_again():
    # Take input from user
    repeat_calculator = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
    
    if repeat_calculator.upper() == 'Y':
        calculate()
    elif repeat_calculator.upper() == 'N':
        print('See you later!')
    else:
        repeat_again()
