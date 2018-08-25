'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
adict = {}
def tokenize(string):
    '''Token'''
    global adict
    string = re.sub('[^A-z,0-9 ]', ' ', string)
    string = string.split()
    for index in string:
        if index not in adict:
            adict[index] = 1
        else:
            adict[index] += 1
        if ',' in adict:
            del adict[',']
    return adict   
def main():
    '''Man'''
    lines = int(input())
    for _ in range(lines):
        line = input()
        string = tokenize(line)
    print(string)


if __name__ == '__main__':
    main()
