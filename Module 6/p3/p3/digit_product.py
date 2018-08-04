'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''Input a number it will return product of all the digits in that number'''
    int_input = int(input())
    y_1 = abs(int_input)
    x_1 = int_input
    mul = 1
    if y_1 == 0:
        print("0")
    while y_1 != 0:
        rem = y_1%10
        mul = mul*rem
        y_1 = y_1//10
    if x_1 > 0:
        print(mul)
    elif int_input < 0:
        print("-"+str(mul))
if __name__ == "__main__":
    main()
