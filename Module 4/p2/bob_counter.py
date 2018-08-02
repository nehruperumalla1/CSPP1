'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob'
occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''Counting no.of bob in given in string'''
    main_str = input()
    sub_str = "bob"
    l = len(main_str)
    l1 = len(sub_str)
    i, j, c = 0, 0, 0
    while i < l-1:
        if main_str[i] == sub_str[j]:
            j += 1
            if j == l1-1:
                c += 1
                j = 0
                i -= 1
        i += 1
    print(c)
if __name__ == "__main__":
    main()
