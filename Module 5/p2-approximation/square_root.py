# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
	numb = int(input())
	epsilon = 0.01
	step = 0.0
	inc = 0.1
	while abs(step**2 - numb)>=epsilon:
		step += inc
	if abs(step**2 - numb) >= epsilon:
		print()
	else:
		print(str(step))

if __name__== "__main__":
	main()
