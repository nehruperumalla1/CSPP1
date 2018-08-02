'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob'
occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    s = input()
    s1 = "bob"
    l = len(s)
    l1 = len(s1)
    i, j, c = 0, 0, 0
    while i < l-1:
        if s[i] == s1[j]:
            j += 1
            if j == l1-1:
                c += 1
                j = 0
                i -= 1
        i += 1
    print(c)
if __name__ == "__main__":
    main()
