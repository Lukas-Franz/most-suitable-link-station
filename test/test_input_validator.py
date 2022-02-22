import unittest

from helper.input_validator import InputValidator

VALID_INPUT = [
    [0, 0, 10],
    [20, -20, 5],
    [10, 0, 12]
]
INVALID_INPUT_FLOAT_NUMBER = [
    [0, 0, 5],
    [5.0, 9, 3]
]
INVALID_INPUT_STRING = [
    [0, 0, 5],
    [8, 5, 'a']
]


class TestInputValidator(unittest.TestCase):
    def test_with_valid_input(self):
        self.assertTrue(InputValidator.validate(VALID_INPUT))

    def test_with_invalid_input_float_numbers(self):
        with self.assertRaises(TypeError):
            InputValidator.validate(INVALID_INPUT_FLOAT_NUMBER)

    def test_with_invalid_input_string(self):
        with self.assertRaises(TypeError):
            InputValidator.validate(INVALID_INPUT_STRING)
