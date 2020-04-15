import unittest
from decimal import Decimal
from decimal_precision import change_precision, ChangePrecision


class TestDecimalPrecision(unittest.TestCase):
    def test_changing_precision_with_correct_with_block(self):
        with change_precision(2):
            result = Decimal('1.123132132') + Decimal('2.23232')

        result2 = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(result, Decimal('3.4'))
        self.assertEqual(result2, Decimal('3.355452132'))

    def test_changing_precision_with_wrong_with_blok(self):
        with self.assertRaises(Exception):
            with change_precision(2):
                raise Exception

        result = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(result, Decimal('3.355452132'))


class TestDecimalPrecisionClass(unittest.TestCase):
    def test_changing_precision_with_correct_with_block(self):
        with ChangePrecision(2):
            result = Decimal('1.123132132') + Decimal('2.23232')

        result2 = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(result, Decimal('3.4'))
        self.assertEqual(result2, Decimal('3.355452132'))

    def test_changing_precision_with_wrong_with_blok(self):
        with self.assertRaises(Exception):
            with ChangePrecision(2):
                raise Exception

        result = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(result, Decimal('3.355452132'))


if __name__ == '__main__':
    unittest.main()
