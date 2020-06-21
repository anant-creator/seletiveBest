''' Exercise Question 10: Remove duplicate from a list and create a tuple and find the minimum and maximum number '''


jo = [12, 23,34, 45, 45, 56, 56]
yo = tuple(set(jo))
print(jo)
print(yo)
print(min(yo))
print(max(yo))
