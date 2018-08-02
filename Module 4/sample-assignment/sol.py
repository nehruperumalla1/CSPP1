# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and
# returns the factorial of given number.

# This function takes in one number and returns one number.

def main():
    data = input()
    print(int(data[0])+int(data[1]))
    for i in range(1, data):
        data=data*i
print(data)
if __name__ == "__main__":
    main()
