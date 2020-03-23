from math import gcd

class Fraction:

	def __init__(self, nom, denom):

		assert denom > 0, 'Zero or negative denominator'

		self.nom = nom
		self.denom = denom


	def simplify_fraction(self):

		d = gcd(self.nom, self.denom)

		return Fraction(self.nom // d, self.denom // d)


	def __add__(self,other):
		return Fraction(self.nom*other.denom + self.denom*other.nom, self.denom*other.denom).simplify_fraction()


	def __str__(self):
		return f'{self.nom}/{self.denom}'


	def __repr__(self):
		return f'Fraction {self}'


	def __eq__(self,other):
		simplified_self = self.simplify_fraction()
		simplified_other = other.simplify_fraction()

		return simplified_self.nom == simplified_other.nom and simplified_self.denom == simplified_other.denom


	def __lt__(self,other):
		first = self.nom / self.denom
		second = other.nom / other.denom

		return first < second


def main():
	fraction = Fraction(3,6)
	fraction1 = Fraction(1,2)
	fraction.simplify_fraction()
	fraction1.simplify_fraction()

	arr = [fraction, fraction1]
	print(sorted(arr))


if __name__ == '__main__':
	main()