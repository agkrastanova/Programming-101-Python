import unittest

from decorator_silence import silence


@silence('errors.txt')
def foo(x):
    if x > 50:
        raise ValueError('Omg.')


foo(100)
foo(10)


class TestSilence(unittest.TestCase):
    def test_silence_should_not_raise_error_but_write_in_the_file(self):
        exc = None

        try:
            foo(100)
        except Exception as err:
            exc = err

        self.assertIsNone(exc)

    def test_silence_with_correct_arguments_should_not_raise_error(self):
        exc = None

        try:
            foo(10)
        except Exception as err:
            exc = err

        self.assertIsNone(exc)


if __name__ == '__main__':
    unittest.main()
