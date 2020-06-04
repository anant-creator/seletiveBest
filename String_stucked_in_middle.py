'''  Exercise Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1  '''


def midremoval():
	a = input("Enter a string here:- ")
	b = input("Enter b string here:- ")
	c = int(len(a) / 2)
	print(a[:c] + b + a[c:])
	
midremoval()
