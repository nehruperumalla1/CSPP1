'''Write a python program to find if the given number is a perfect'''
#cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
def main():
    '''Enter a input this will displays is it perfect cube or not'''
    number = int(input())
    itr = 0
    while itr <= number:
        if itr**3 == number:
            flag = 0
            print(str(number) + " is a perfect cube")
            break
        else:
            flag = 1
        itr += 1
    if flag == 1:
        print(str(number)+" is not a perfect cube")
if __name__ == "__main__":
    main()
