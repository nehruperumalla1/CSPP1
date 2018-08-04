'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''Input a number it will return product of all the digits in that number'''
    int_input = int(input())
    y=abs(int_input)
    x = int_input
    mul = 1
    if y == 0:
    	print("0")
    while y!=0:
        rem = y%10
        mul = mul*rem
        y = y//10
    if x > 0:
    	print(mul)
    elif int_input < 0:
    	print("-"+str(mul))
if __name__ == "__main__":
    main()
