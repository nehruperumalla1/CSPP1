'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob'
occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''Counting no.of bob in given in string'''
    str1 = input()
    count = 0
    index = str1.find("bob")
    while index >= 0:
        count = count+1
        index = str1.find("bob", index+2)
    print(count)
if __name__ == "__main__":
    main()
