''' Exercise Question 6: Given a following two sets find the intersection and remove those elements from the first set '''

first = [12, 34, 45, 56, 67, 78]
second = [98, 78, 76, 65, 45, 43]
do = set(first)
yo = []


for i in first:
	for j in second:
		if i == j:
			do.remove(i)
			yo.append(i)
			
			
			
print(set(yo))	
print(do)
