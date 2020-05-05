import sys

def sum_numbers():
	Sum = 0
	with open(sys.argv[1],'r') as f:
		for line in f:
			for num in line.split():
				Sum += int(num)

	print('Sum: ', Sum)



def main():
	sum_numbers()


if __name__ == '__main__':
	main()