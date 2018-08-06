p = 3329
intr = 0.2
mi = intr/12
upb = p 
s = 0
for i in range (12,0,-1):
	print(i,"---"+str(upb))
	up = (upb+(upb*mi))//i
	s+=up
	upb = upb-up

print(s/12)
