''' Exercise: PowerIter'''
# Write a Python function, iterPower(base, exp), that takes in two numbers
# and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.
def iterpower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Your code here
    base1 = base
    if exp == 0:
        return 1
    else:
        for _ in range(exp-1):
            base = base*base1
        return base
def main():
    '''Main function for Power using Iteration'''
    data = input()
    data = data.split(" ")
    print(iterpower(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
