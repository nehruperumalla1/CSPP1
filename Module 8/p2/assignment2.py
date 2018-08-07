'''Exercise: Assignment-2'''
# Write a Python function, sumofdigits, that takes in one
# number and returns the sum of digits of given number.

# This function takes in one number and returns one number.
def sumofdigits(n_1, sum1):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n_1 == 0:
        return sum1
    k_1 = n_1%10
    sum1 = sum1+k_1
    n_1 = n_1//10
    return sumofdigits(n_1, sum1)
def main():
    '''Main Function'''
    a_1 = input()
    sum1 = 0
    print(sumofdigits(int(a_1), sum1))
if __name__ == "__main__":
    main()
