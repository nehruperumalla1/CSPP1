varA="Hello"
varB="World"

if isinstance(varA,str) or isinstance(varB,str):
	print("string involved")
	if varA>varB:
		print("Bigger")
	if varA==varB:
		print("equal")
	if varA<varB:
		print("smaller")