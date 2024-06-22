from utils import *

        
# Define calculate function
def calculate():
    operation = enter_valid_operation_input()
    print(operation)
    # Add repeat function to calculate() function
    repeat_again()


# Define a repeat_again function to call the calculate function repeatedly
def repeat_again():
    while True:
        # Take input from user
        repeat_calculator = input('''
        Do you want to calculate again?
        Please type Y for YES or N for NO.
        ''').strip().upper()
        
        if repeat_calculator == 'Y':
            calculate()
        elif repeat_calculator == 'N':
            print('Exiting calculator. Goodbye!')
            break
        else:
            print("Invalid input. Please enter Y or N.")


if __name__ == '__main__':
    welcome()
    # Call the calculate function
    calculate()
    