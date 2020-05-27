''' create a user input array '''
from array import *

a = array("i", [])
b = int(input("Tell me how many elements your array should have:- "))
for i in range(b):
	c = int(input("Enter a value:- "))
	a.append(c)
	
print(a)
