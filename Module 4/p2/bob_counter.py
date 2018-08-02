'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob'
occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''Counting no.of bob in given in string'''
    main_str = input()
    sub_str = "bob"
    length_main = len(main_str)
    length_sub = len(sub_str)
    i, j, count = 0, 0, 0
    while i < length_main-1:
        if main_str[i] == sub_str[j]:
            j += 1
            if j == length_sub-1:
                count += 1
                j = 0
                i -= 1
        i += 1
    print(count)
if __name__ == "__main__":
    main()
