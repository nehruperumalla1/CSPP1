''' Exercise: PowerRecr'''
# Write a Python function, recurPower(base, exp), that takes in two numbers
# and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def recurpower(base, exp, base1):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        base = base*base1
        return recurpower(base, exp-1, base1)
def main():
    '''Main Function'''
    data = input()
    data = data.split(" ")
    #base1=data[0]
    print(recurpower(float(data[0]), int(data[1]), float(data[0])))
if __name__ == "__main__":
    main()
