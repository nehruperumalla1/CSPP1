#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
#your program should print:

#Number of vowels: 5

def main():
    '''Finding no.of Vowels'''
    s = input()
    l = len(s)
    j = 0
    for i in range(0, l):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            j += 1
    print(str(j))
if __name__ == "__main__":
    main()
