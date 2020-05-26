''' Question 1: Accept two integer numbers from a user and return their product and  if the product is greater than 1000,
then return their sum. '''

a = int(input("Enter a number:- "))
b = int(input("Enter a number:- "))
product = (a * b)
if product < 1000:
    print(product)
else:
		print(a + b)

