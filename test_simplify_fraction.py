import unittest

from simplify_fraction import (simplify_fraction_func, validate_arguments, collect_fractions,sum_two_fractions)


class TestValidateArguments(unittest.TestCase):

	def test_if_arguments_are_not_integers_raise_error(self):

		fraction = ('a',1)

		exc = None

		try:
			validate_arguments(fraction)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid argument')




class TestSimplifyFraction(unittest.TestCase):


	def test_if_denominator_is_zero_raise_error(self):

		fraction = (3,9)

		fraction = simplify_fraction_func(fraction)

		flag = False
		if fraction[1] == 0:
			flag = True


		self.assertFalse(flag)


	def test_if_simplify_correctly(self):

		fraction = (3,9)


		result = simplify_fraction_func(fraction)


		self.assertEqual(result,(1,3))



class TestCollectionFraction(unittest.TestCase):

	def test_if_all_arguments_are_simplified(self):
		fractions = [(1,3),(1,4),(3,7)]
		temp_list = []
		
		
		for fraction in fractions:
			temp_elem = simplify_fraction_func(fraction)
			temp_list.append(temp_elem)



		self.assertEqual(fractions, temp_list)

	def test_if_calculates_fractions_correctly(self):
		fractions = [(1,4),(1,2)]

		Sum = sum_two_fractions(fractions[0],fractions[1])

		self.assertEqual(Sum,(3,4))



if __name__ == '__main__':
	unittest.main()