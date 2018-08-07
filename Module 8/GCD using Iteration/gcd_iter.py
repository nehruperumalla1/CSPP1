''' Exercise: GCDIter'''
# Write a Python function, gcdIter(a, b), that takes in two numbers and
# returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcditer(a_1, b_1):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    for i_1 in range(1, max(a_1, b_1)+1):
        if a_1%i_1 == 0 and b_1%i_1 == 0:
            number = i_1
    return number
def main():
    '''Main Function'''
    data = input()
    data = data.split()
    print(gcditer(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
