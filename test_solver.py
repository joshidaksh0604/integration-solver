import unittest

import validator
import coeff_pow_extract as extract
import polynomial as poly


class TestValidator(unittest.TestCase):

    def test_valid_expression(self):
        valid, message = validator.validate_exp('3x^2+4x-7')
        self.assertTrue(valid)

    def test_valid_expression_with_multiplication(self):
        valid, message = validator.validate_exp('3*x^2+4*x-7')
        self.assertTrue(valid)

    def test_invalid_character(self):
        valid, message = validator.validate_exp('3y^2+4')
        self.assertFalse(valid)

    def test_invalid_power(self):
        valid, message = validator.validate_exp('3x^^2')
        self.assertFalse(valid)

    def test_empty_expression(self):
        valid, message = validator.validate_exp('')
        self.assertFalse(valid)


class TestParser(unittest.TestCase):

    def test_parser(self):
        result = extract.coeff_power('3x^2+4x-7')

        expected = [
            [3, 2],
            [4, 1],
            [-7, 0]
        ]

        self.assertEqual(result, expected)

    def test_parser_without_coefficients(self):
        result = extract.coeff_power('x^3-x+5')

        expected = [
            [1, 3],
            [-1, 1],
            [5, 0]
        ]

        self.assertEqual(result, expected)


class TestPolynomial(unittest.TestCase):

    def test_basic_integration(self):
        expression = [
            [3, 2],
            [4, 1],
            [-7, 0]
        ]

        result = poly.basic_polynomial(expression)

        expected = [
            [1.0, 3],
            [2.0, 2],
            [-7.0, 1]
        ]

        self.assertEqual(result, expected)

    def test_constant_integration(self):
        expression = [
            [7, 0]
        ]

        result = poly.basic_polynomial(expression)

        expected = [
            [7.0, 1]
        ]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()