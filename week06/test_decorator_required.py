import unittest

from decorator_required import required


class Animal:
    @required
    def eat(self, food):
        pass


class Panda(Animal):
    pass


p = Panda()


class TestRequiredDecorator(unittest.TestCase):
    def test_decorator_required_should_raise_error_if_function_is_not_overrided_in_child(self):
        exc = None

        try:
            p.eat()
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'All classes that inherit from "Panda" must provide "eat" method.')


if __name__ == '__main__':
    unittest.main()
