import unittest
from time import sleep

from decorator_performance import performance


@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"


class TestPerformace(unittest.TestCase):
    def test_performance_decorator_works_as_expected(self):
        result = something_heavy()

        expected = 'I am done!'

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
