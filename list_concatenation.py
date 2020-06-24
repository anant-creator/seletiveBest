''' Exercise Question 2: Concatenate two lists index-wise '''

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
#Type 1
list3 = [i + j for i,j in zip(list1, list2)]
print(list3)

#Type 2
n = 1    
for i in list2:
    list1.insert(n, i)
    n += 2
l = ""
l = l.join(list1)
print(l)
#Type 3
for i in range(len(list1)):
    list1[i] += list2[i]
    
print(list1)
