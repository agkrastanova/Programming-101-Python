import unittest
import sys

from polynomials import Polynomials


class TestPolynomialsClass(unittest.TestCase):

	def test_string_representation_is_as_expected_one(self):

		polynomial = Polynomials('3*x^2 + 2*x^1 + 3')

		self.assertEqual(str(polynomial), '3*x^2 + 2*x^1 + 3')

	def test_derivate_function_with_constant_value(self):

		polynomial = Polynomials('3')

		result = polynomial.derivate()

		self.assertEqual(result, '0')

	def test_derivate_function_with_x_pow_one(self):

		polynomial = Polynomials('x')

		result = polynomial.derivate()

		self.assertEqual(result, '1')

	def test_derivate_function_with_x_pow_int(self):

		polynomial = Polynomials('x^3')

		result = polynomial.derivate()

		self.assertEqual(result, '3*x^2')

	def test_derivate_function_with_one_polinomial_term(self):
		polynomial = Polynomials('3*x^3')

		result = polynomial.derivate()

		self.assertEqual(result, '9*x^2')

	def test_derivate_function_with_more_terms(self):

		polynomial = Polynomials('3*x^2 + 2*x^2 + x^3 + x^1 + 3*x^1 + 2')

		result = polynomial.derivate()

		self.assertEqual(result,'6*x^1 + 4*x^1 + 3*x^2 + 1 + 3')


if __name__ == '__main__':
	unittest.main()