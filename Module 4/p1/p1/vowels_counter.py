'''Assume s is a string of lower case characters.'''

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
#your program should print:

#Number of vowels: 5

def main():
    '''Finding no.of Vowels'''
    s_1 = input()
    l_1 = len(s_1)
    j = 0
    for i in range(0, l_1):
        if s_1[i] == 'a' or s_1[i] == 'e' or s_1[i] == 'i' or s_1[i] == 'o' or s_1[i] == 'u':
            j += 1
    print(str(j))
if __name__ == "__main__":
    main()
