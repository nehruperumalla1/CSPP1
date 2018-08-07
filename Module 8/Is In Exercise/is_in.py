'''Exercise: Is In'''
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String
#and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.
def isin(char, astr, i_1):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if char == astr[i_1]:
        return True
    if i_1 < len(astr)-1:
        if char != astr[i_1]:
            return isin(char, astr, i_1+1)
    return False
def main():
    '''Main Function for char checker'''
    data = input()
    data = data.split()
    a_1 = 0
    print(isin((data[0]), data[1], a_1))
if __name__ == "__main__":
    main()
