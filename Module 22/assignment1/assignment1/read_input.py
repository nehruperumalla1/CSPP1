'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
	'''Main Function'''
	lines = int(input())
	for i in range(lines):
		line = input()
		print(line)

if __name__ == '__main__':
    main()
