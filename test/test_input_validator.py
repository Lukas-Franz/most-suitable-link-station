import unittest

from input_validator import InputValidator

VALID_INPUT = [
    [0, 0, 10],
    [20, 20, 5],
    [10, 0, 12]
]
INVALID_INPUT_NEGATIVE_NUMBER = [
    [0, 0, 5],
    [-1, 9, 3]
]
INVALID_INPUT_STRING = [
    [0, 0, 5],
    [8, 5, 'a']
]


class TestInputValidator(unittest.TestCase):
    def test_with_valid_input(self):
        self.assertTrue(InputValidator.validate(VALID_INPUT))

    def test_with_invalid_input_negative_numbers(self):
        with self.assertRaises(ValueError):
            InputValidator.validate(INVALID_INPUT_NEGATIVE_NUMBER)

    def test_with_invalid_input_string(self):
        with self.assertRaises(ValueError):
            InputValidator.validate(INVALID_INPUT_STRING)
