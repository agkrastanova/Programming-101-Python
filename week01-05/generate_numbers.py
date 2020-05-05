import sys
from random import randint

def generate_number():
	number = int(sys.argv[2])

	with open(sys.argv[1], 'a') as f:
		while number > 0:
			n = str(randint(1, 1000))
			f.write(n)
			f.write(" ")
			number-=1

def main():
	generate_number()


if __name__ == '__main__':
	main()