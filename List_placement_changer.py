''' Exercise Question 2: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list '''


iit = [12, 24, 36, 48, 60, 72, 84, 96]
j = iit[4]
print(j)
iit.remove(iit[4])
iit.insert(2, j)
iit.append(j)
print(iit)
