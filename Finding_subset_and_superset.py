''' Exercise Question 7: Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set '''

a = {12, 23, 24}
b = {23, 24, 25}
c = {12, 24, 25, 67, 45, 56}
count = 0
for i in a:
	for j in c:
		if i == j:
			count += 1
			if count == len(a):
				print(a)
				print(c)
				print("1st set is a substring")
				print("Set c is the super set of set a")
for i in b:
	for j in c:
		if i == j:
			count += 1
			if count == len(b):
				print(b)
				print(c)
				print("2nd set is a substring")
				print("Set c is the super set of set c")
				
