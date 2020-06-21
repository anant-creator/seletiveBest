''' Exercise Question 9: Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates '''


a = {"jan":12, "feb":23, "mar":34, "apr":45, "may":45, "june":56}
b = []
for i in a.values():
	if i not in b:
		b.append(i)
		
print(b)
