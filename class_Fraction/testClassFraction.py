import unittest

from classFraction import Fraction


class TestFractionClass(unittest.TestCase):

	def test_cannot_instantiate_fraction_with_zero_denominator(self):

		exception = None

		try:
			Fraction(1,0)
		except AssertionError as exc:
			exception = exc

		self.assertIsNotNone(exception)


	def test_fraction_string_representation_is_as_expected_one(self):

		fraction1 = Fraction(1,3)
		fraction2 = Fraction(-1,3)
		fraction3 = Fraction(2,4)

		self.assertEqual(str(fraction1),'1/3')
		self.assertEqual(str(fraction2),'-1/3')
		self.assertEqual(str(fraction3),'2/4')


	def test_fraction_equlization_with_equal_fraction(self):

		fraction1 = Fraction(1,3)
		fraction2 = Fraction(1,3)

		self.assertTrue(fraction1 == fraction2,'Fractions are not equal')


	def test_fraction_equalizations_with_equal_non_simplified_fractions(self):

		fraction1 = Fraction(1,3)
		fraction2 = Fraction(3,9)

		self.assertTrue(fraction1 == fraction2, 'Fractions are not equal')


	def test_simplified_fraction_is_preserved_after_simplification(self):

		fraction = Fraction(1,5)

		expected = Fraction(1,5)

		self.assertEqual(fraction.simplify_fraction(), expected)


	def test_fraction_is_simplified_as_expected(self):

		fraction = Fraction(20,100)

		expected = Fraction(1,5)

		self.assertEqual(fraction.simplify_fraction(),expected)


	def test_addition_fractions_works_correct_for_non_simplified_result_with_equal_denominator(self):

		fraction1 = Fraction(1,5)
		fraction2 = Fraction(2,5)

		result = fraction1 + fraction2

		self.assertEqual(result,Fraction(3,5))


	def test_addition_fractions_works_correct_for_non_simplified_result_with_non_equal_denominator(self):

		fraction1 = Fraction(1,7)
		fraction2 = Fraction(2,6)

		result = fraction1 + fraction2

		self.assertEqual(result.nom,10)
		self.assertEqual(result.denom, 21)


	def test_fraction_comparison_works_correctly_for_siplified_fractions(self):
		fraction1 = Fraction(1,3)
		fraction2 = Fraction(1,2)

		result = fraction1 < fraction2

		self.assertTrue(result, 'Fraction1 is not less than Fraction2')


	def test_fraction_comparison_works_correctly_for_non_siplified_fractions(self):
		fraction1 = Fraction(3,9)
		fraction2 = Fraction(2,4)

		result = fraction1 < fraction2

		self.assertTrue(result)




if __name__ == '__main__':
	unittest.main()
