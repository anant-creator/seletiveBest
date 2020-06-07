''' Exercise Question 7: String characters balance Test '''

def balance():
	a = input("Enter a string:- ")
	b = input("enter some with one space between:- ")
	b = b.split()
	d, e = b[0], b[1]
	if d in a and e in a:
		print("Balanced")
	else:
		print("Non Balanced")
	
balance()
	
