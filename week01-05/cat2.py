import sys

def cat2():
	for i in range(1,len(sys.argv)):
	 	with open(sys.argv[i], 'r') as f:
	 		print(f.read())


def main():
	cat2()


if __name__ == '__main__':
	main()