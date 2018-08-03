'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur
in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a
different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    '''Alphabet Sequence in a given String'''
    str1 = input()
    i, j, temp1, temp2 = 0, 0, 0, 0
    len_main = len(str1)
    while i < len_str1-1:
        if str1[i] <= str1[i+1]:
            temp1 += 1
            if temp1 > temp2:
                temp2 = temp1
                j = i+1
        else:
            temp1 = 0
        i += 1
    string = j-temp2
    print(str1[string:j+1])

if __name__ == "__main__":
    main()
