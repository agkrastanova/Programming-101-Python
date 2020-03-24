import sys

class Polynomials:

	def __init__(self,polynomial):

		self.polynomial = polynomial


	def __str__(self):
		return str(self.polynomial)

	
	def derivate(self):

		polynomial_list = self.polynomial.split(' + ')

		derivated_list = []

		for polynomial in polynomial_list:
			if polynomial == 'x':
				derivated_list.append('1')
			elif len(polynomial) == 1: 
				continue
			elif len(polynomial) == 3:
				if polynomial[-1] == 1:
					derivated_list.append('1')
					continue
				else:
					new_coef = int(polynomial[-1])
					power = new_coef - 1
					if power == 0:
						derivated_list.append(str(new_coef))
						continue
					elif power == 1:
						new_powerX = str(new_coef) + 'x'
						derivated_list.append(str(new_powerX))
						continue
					else:
						new_powerX = str(new_coef) +'*x^' + str(power)
						derivated_list.append(new_powerX)
						continue
			else:		
				polynomial_parts = polynomial.split('*')
				powerX = polynomial_parts[-1]
				power = int(polynomial_parts[1][-1])
				new_coef = int(polynomial_parts[0])
				new_coef *= power
				power -= 1
				if power == 0:
					new_powerX = str(new_coef)
					derivated_list.append(new_powerX)
				else:
					new_powerX = str(new_coef)+ '*x^' + str(power)
					derivated_list.append(new_powerX)


		if len(derivated_list) == 0:
			return '0' 

		derivated_string = derivated_list[0]

		for i in range(1,len(derivated_list)):
			derivated_string += ' + '
			derivated_string += str(derivated_list[i])

		return derivated_string


def print_func():

	derivate_string = sys.argv[1]
	polynomial = Polynomials(derivate_string)

	derivated_string = polynomial.derivate()

	return f'Derivative of f(x) = {polynomial} is:\nf\'(x) = {derivated_string}'


def main():
	print(print_func())


if __name__ == '__main__':
	main()
