import unittest
from unittest.mock import patch
import sys

# Import the functions to be tested
sys.path.insert(0, '../calculator')  # Adjust path as needed
from utils import enter_valid_operation_input, enter_valid_number_input
from operations import addition, subtraction, multiplication, division, power, modulus, absolute, inverse


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(4, 5), 9)
        self.assertEqual(addition(1, -1.0), 0.0)

    def test_subtraction(self):
        self.assertEqual(subtraction(3.2, 2), 1.2000000000000002)
        self.assertEqual(subtraction(-1, 1), -2)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3.5), 7.0)
        self.assertEqual(multiplication(0, 3), 0)

    def test_division(self):
        self.assertEqual(division(6.3, -4), -1.575)
        self.assertEqual(division(1, 0), "Error: division by zero")

    def test_power(self):
        self.assertEqual(power(4, 5.0), 1024.0)
        self.assertEqual(power(-3, -3), -0.037037037037037035)

    def test_modulus(self):
        self.assertEqual(modulus(5, 6.5), 5.0)
        self.assertEqual(modulus(4, 0), "Error: division by zero")

    def test_absolute(self):
        self.assertEqual(absolute(-9), 9)
        self.assertEqual(absolute(7.9), 7.9)

    def test_inverse(self):
        self.assertEqual(inverse(5), 0.2)
        self.assertEqual(inverse(-8.5), -0.11764705882352941)

    @patch('builtins.input', side_effect=['+', '6', '7'])
    def test_enter_valid_operation_addition_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), 13)

    @patch('builtins.input', side_effect=['-', '5.5', '4'])
    def test_enter_valid_operation_subtraction_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), 1.5)

    @patch('builtins.input', side_effect=['*', '3.4', '5.2'])
    def test_enter_valid_operation_multiplication_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), 17.68)

    @patch('builtins.input', side_effect=['/', '-3.4', '0'])
    def test_enter_valid_operation_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), 'Error: division by zero')

    @patch('builtins.input', side_effect=['**', '-4', '6'])
    def test_enter_valid_operation_power_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), 4096)

    @patch('builtins.input', side_effect=['%', '-4', '6'])
    def test_enter_valid_operation_modulus_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), 2)

    @patch('builtins.input', side_effect=['abs', '-4'])
    def test_enter_valid_operation_absolute_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), 4)

    @patch('builtins.input', side_effect=['inv', '-4'])
    def test_enter_valid_operation_inverse_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), -0.25)

    @patch('builtins.input', side_effect=['inv', '0'])
    def test_enter_valid_operation_inverse_zero_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), "Error: division by zero")

    # noinspection PyUnusedLocal
    @patch('builtins.input', side_effect=['()'])
    def test_enter_valid_operation_invalid_input(self, mock_input):
        self.assertEqual(enter_valid_operation_input(), "Error: () is not a valid operation")

    # noinspection PyUnusedLocal
    @patch('builtins.input', side_effect=['10'])
    def test_enter_valid_number_integer_input(self, mock_input):
        # noinspection PyArgumentList
        self.assertEqual(enter_valid_number_input('Enter a number: '), 10)

    # noinspection PyUnusedLocal,PyArgumentList
    @patch('builtins.input', side_effect=['-9.3'])
    def test_enter_valid_number_float_input(self, mock_input):
        # noinspection PyArgumentList
        self.assertEqual(enter_valid_number_input('Enter a number: '), -9.3)

    # noinspection PyUnusedLocal
    @patch('builtins.input', side_effect=['Y', 'N'])
    @patch('calculator.calculate')
    def test_repeat_again(self, mock_calculate, mock_input):
        from calculator import repeat_again
        repeat_again()
        mock_calculate.assert_called_once()


if __name__ == '__main__':
    unittest.main()
