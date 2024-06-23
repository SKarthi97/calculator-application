from operations import *


# Define core logic for the calculator application
def perform_operations(operation, number_1, number_2=None):
    operations = {'+': addition,
                  '-': subtraction,
                  '*': multiplication,
                  '/': division,
                  '^': power,
                  'Mod': modulus,
                  'abs': absolute,
                  'inv': inverse,
                  'n!': factorial,
                  'exp': exponential,
                  'log': natural_log}

    if operation not in operations:
        return f"Error: {operation} is not valid operation"

    try:
        if operation in ['abs', 'inv', 'n!', 'log', 'exp']:
            return operations[operation](number_1)
        else:
            return operations[operation](number_1, number_2)
    except ZeroDivisionError as e:
        return f"Error : {e}"
    except ValueError as e:
        return f"Error : {e}"
