operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

   
def addition(number_1, number_2):
    # return number_1 + number_2
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

def subtraction(number_1, number_2):
    # return number_1 - number_2
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
    
def multiplication(number_1, number_2):
    # return number_1 * number_2
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

def division(number_1, number_2):
    # return number_1 / number_2
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
    
try:
    number_1 = int(input('Enter your first number: '))
except ValueError:
    print("Invalid number")
    
try:
    number_2 = int(input('Enter your second number: '))
except ValueError:
    print("Invalid number")

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