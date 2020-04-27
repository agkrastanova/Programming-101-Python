import unittest
from unittest.mock import patch
from big_positive_pow import big_possitive_pow


class TestBigPositivePow(unittest.TestCase):
    @patch('big_positive_pow.randint')
    def test_if_randint_y_value_is_less_than_one_should_raise_error(self, mock_randint):
        mock_randint.return_value = -1
        exc = None

        try:
            big_possitive_pow()
        except Exception as e:
            exc = e

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Try again.')

    @patch('big_positive_pow.randint')
    def test_function_should_raise_number_to_the_power_of_y(self, randint_mock):
        randint_mock.return_value = 3

        result = big_possitive_pow()

        self.assertEqual(result, 27)


if __name__ == '__main__':
    unittest.main()
