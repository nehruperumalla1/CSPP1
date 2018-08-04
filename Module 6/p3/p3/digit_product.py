'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''Input a number it will return product of all the digits in that number'''
    int_input = int(input())
    mul = 1
    while abs(int_input)!=0:
        rem = int_input%10
        mul = mul*rem
        int_input = int_input//10
    if int_input != 0:
    	print(mul)
    elif int_input == 0:
    	print("0")
    elif int_input < 0:
    	print("-"+mul)
if __name__ == "__main__":
    main()
