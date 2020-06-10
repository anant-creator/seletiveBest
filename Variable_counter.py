''' Exercise Question 10: Given an input string, count occurrences of all characters within a string '''


a = input("Enter a string to count:- ")
c = []
d = []
for i in a:
  b = a.count(i)
  if i not in c:
    c.append(i)
    d.append(b)
    e = dict(zip(c, d))
print(e)
