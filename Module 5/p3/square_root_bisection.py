'''Write a python program to find the square root of the
given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''Square root using bisection'''
    sroot = int(input())
    epsilon = 0.01
    #step = 0.1
    start = 0
    end = sroot
    root = (start+end)/2
    while abs(root**2-sroot) >= epsilon:
        if root**2 < sroot:
            start = root
        else:
            end = root
        root = (start+end)/2
    print(str(root))
if __name__ == "__main__":
    main()
