'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Enter a string includes special characters, this will display special charcaters 
    replaced with spaces
    '''
    str_input = input()
    length = len(str_input)
    d_1 = ''
    for i in str_input:
        if i in "!@#$%^&*":
            d_1 += " "
        else:
            d_1 += i
    print(d_1)
if __name__ == "__main__":
    main()
