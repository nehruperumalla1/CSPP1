#define the gen_primes function here
# def prime(n):

# 	for a in range(2,n):
# 		if n%a == 0:
# 			return False
# 	return True

def genPrimes():
	num = 2
	while num>0:
		prime = True
		for index in range(2,num):
			if num%index == 0:
				prime = False
		if prime:
			yield num
		num += 1

def main():
	data = input()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p=primeGenerator.__next__()
	    if(i%b==0):
	        print(p)
	
if __name__== "__main__":
	main()
