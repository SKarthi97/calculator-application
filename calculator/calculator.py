from operations import *


# Define calculate function
def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
        
    try:
        number_1 = int(input('Enter your first number: '))
    except ValueError:
        print("Invalid number")
        number_1 = 0
        
    try:
        number_2 = int(input('Enter your second number: '))
    except ValueError:
        print("Invalid number")
        number_2 = 1

    if operation == '+':
        addition(number_1, number_2)
    elif operation == '-':
        subtraction(number_1, number_2)
    elif operation == '*':
        multiplication(number_1, number_2)
    elif operation == '/':
        division(number_1, number_2)
    else:
        print('You have not typed a valid operator, please run the program again.')
    
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


# Call the calculate function
calculate()