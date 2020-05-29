''' Create a programme to find the factorial of a number '''
def fact(n):
	a = 0
	
	for i in range(n-1):
		if a <= n:
			a += 1
			n *= a
	print(n)
		
fact(7)
