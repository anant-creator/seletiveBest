''' Exercise Question 8: Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list '''


jo =[12, 23, 34, 45, 56, 67, 78, 89]
lo = {"creep":23, "sweep":45, "deep":67, "weep":89}
io = list(lo.values())

for i in jo:
	for j in io:
		if i != j and i in jo:
			jo.remove(i)
			
print(jo)
