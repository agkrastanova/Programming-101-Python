import math

def validate_arguments(fraction):

	if fraction[0] is not int:
		raise ValueError('Invalid argument')
	if fraction[1] is not int:
		raise ValueError('Invalid argument')

	return True


def simplify_fraction_func(fraction):
	l = list(fraction)


	d = math.gcd(l[0], l[1])


	l[0] = int(l[0]) // d
	l[1] = int(l[1]) // d


	return tuple(l)

def sum_two_fractions(fraction1,fraction2):

	nom1 = fraction1[0]
	denom1 = fraction1[1]

	nom2 = fraction2[0]
	denom2 = fraction2[1]

	new_nom = nom1*denom2 + nom2*denom1
	new_denom = denom1*denom2

	answer = (new_nom,new_denom)
	answer = tuple(answer)

	answer = simplify_fraction_func(answer)

	return answer


def collect_fractions(fractions):

	temp = []
	for fraction in fractions:
		temp_elem = simplify_fraction_func(fraction)
		temp.append(temp_elem)


	Sum = (0,1)
	current_sum = (0,1)

	for i in range(len(fractions)-1):
		current_sum = sum_two_fractions(fraction[i],fraction[i+1])
		sum_two_fractions(Sum,current_sum)
		print(Sum)

	return Sum



def main():
	#print(simplify_fraction_func((1,4)))
	print(collect_fractions([(1,2),(1,4)]))
	#print(sum_two_fractions((1,4),(1,2)))

if __name__ == '__main__':
	main()