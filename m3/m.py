divisor=2
for num in range(0, 10, 2):
	print(num/divisor)
#---------------------------------------------------------
n=0
if(n%4==0):
	print(n)
if(n%16==0):
	print(n)
#------------------------------------------------
a=int(input())
count,i,s=0,0,0
while count<a:
	if i%2==0:
		s=s+i
		count += 1
	i += 1
print(s)
#-------------------------------------------------
a=int(input())
s,count,i=0,0,0
while count<a:
	s=s+i
	i=i+2
	count += 1
print(s)