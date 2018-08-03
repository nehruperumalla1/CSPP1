#Guess My Number Exercise

def main():
	print("Think of a Num")
	low=1
	high=100
	eps=0.001
	ans=(low+high)//2
	print(ans)
	while ans*2 >= eps:
		s = input()
		if s == 'l':
			low=ans
		elif s == 'h':
			high=ans
		elif s == 'c':
			print("Guess Correct")
			break
		ans=(low+high)//2
		print(ans)
if __name__== "__main__":
	main()