'''  Exercise Question 4: arrange String characters such that lowercase letters should come first  '''


a = input("Enter a string here:- ")
b = list(a)
b.sort()
c = " "
for i in b:
	c += i
print(c)
