'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
adict = {}
def tokenize(string):
	global adict
	string = string.split()
	for index in range(len(string)):
		string1 = re.sub('[^A-z,0-9 ]', '', string[index])
		if string1 not in adict:
			adict[string1] = 1
		else:
			adict[string1] += 1


	
	return adict   
def main():
	lines = int(input())
	for index in range(lines):
		line = input()
		string = tokenize(line)
	print(string)


if __name__ == '__main__':
    main()
