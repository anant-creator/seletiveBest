''' user input list even odd finder '''


list = []
a = int(input("count of elements in list:- "))
even = 0
odd = 0
for i in range(a):
	b = int(input("Enter a value for list:- "))
	list.append(b)
	print(list)
for j in list:
	if j%2==0:
		even+=1
	else:
		odd+=1
		
			
print(list, "in this list we have even : {:d} numbers and odd : {:d} numbers".format(even, odd))
