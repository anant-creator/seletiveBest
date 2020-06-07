''' Exercise Question 1: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second. '''


listup = [12,20,26,50,69,98,45, 76,78]
listset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
hist = []
j = -1
for i in listup:
	j += 1
	if j % 2 == 1:
		hist.append(listup[j])
	
l = -1
for k in listset:
	l += 1
	if l % 2 == 0:
		hist.append(listset[l])
	
	
print(hist)
