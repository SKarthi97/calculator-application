import math


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is undefined")
    return x / y


def power(x, y):
    return x ** y


def modulus(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is undefined")
    return x % y


def absolute(x):
    return abs(x)


def inverse(x):
    if y == 0:
        raise ZeroDivisionError("Inverse of zero is undefined")
    return 1 / x


def factorial(x):
    if x < 0:
        raise ValueError("Factorial of a negative number is undefined")
    return math.factorial(x)


def exponential(x):
    return math.exp(x)


def natural_log(x):
    if x <= 0:
        raise ValueError("Natural logarithm of non-positive number is undefined")
    return math.log(x)
