''' Exercise: GCDRecr '''
# Write a Python function, gcdRecur(a, b), that takes in
# two numbers and
# returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.
Gcd_Nums = []
def gcdrecur(a_1, b_1, i_1):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor
    # of a & b.
    '''
    # Your code here
    #global i,gcdnums
    i_1 += 1
    if i_1 > a_1:
        if len(Gcd_Nums) == 1:
            return 1
        else:
            return max(Gcd_Nums)
    else:
        if a_1%i_1 == 0 and b_1%i_1 == 0:
            Gcd_Nums.append(i_1)
            return gcdrecur(a_1, b_1, i_1)
        return gcdrecur(a_1, b_1, i_1)
def main():
    '''Main Function'''
    data = input()
    data = data.split()
    i_1 = 0
    print(gcdrecur(int(data[0]), int(data[1]), i_1))
if __name__ == "__main__":
    main()
