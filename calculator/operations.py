def addition(number_1, number_2):
    return number_1 + number_2


def subtraction(number_1, number_2):
    return number_1 - number_2


def multiplication(number_1, number_2):
    return number_1 * number_2


def division(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error: division by zero"


def power(number_1, number_2):
    return number_1 ** number_2


def modulus(number_1, number_2):
    try:
        return number_1 % number_2
    except ZeroDivisionError:
        return "Error: division by zero"


def absolute(number):
    return abs(number)


def inverse(number):
    try:
        return 1 / number
    except ZeroDivisionError:
        return "Error: division by zero"
