import math


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
        return "Error: denominator is zero"


def power(number_1, number_2):
    return number_1 ** number_2


def modulus(number_1, number_2):
    try:
        return number_1 % number_2
    except ZeroDivisionError:
        return "Error: denominator is zero"


def absolute(number):
    return abs(number)


def inverse(number):
    try:
        return 1 / number
    except ZeroDivisionError:
        return "Error: denominator is zero"


def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    elif number > 0 and number % 1 == 0:
        Factorial = 1
        while number > 1:
            Factorial *= number
            number -= 1
        return Factorial
    else:
        return "Error: Negative integer or float value is passed"


def exponential(number):
    return math.exp(number)

def log_base_e(number):
    try:
        return math.log(number)
    except ValueError as e:
        return f"Error: {e}"
