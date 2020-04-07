import unittest

from Decorators import accepts


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))


class TestDecorators(unittest.TestCase):
    def test_decorator_accepts_with_say_hello_should_raise_error_if_type_argument_is_not_as_expected_one(self):
        exc = None

        try:
            say_hello(4)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument 4 of say_hello is not str!')

    def test_decorator_accepts_with_say_hello_with_string_type_argument_should_work_correctly(self):
        result = say_hello('Ani')

        expected = 'Hello, I am Ani'

        self.assertEqual(result, expected)

    def test_accepts_decorator_with_deposit_should_raise_error_in_case_of_wrong_type_name(self):
        exc = None

        try:
            deposit(123, 10)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument 123 of deposit is not str!')

    def test_accepts_decorator_with_deposit_should_raise_error_in_case_of_wrong_type_money(self):
        exc = None

        try:
            deposit('Ani', 'ten')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument ten of deposit is not int!')


if __name__ == '__main__':
    unittest.main()
