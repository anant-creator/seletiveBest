'''  Exercise create to user input dictionary a them create a dictionary from it ''' 

a = []
b = []

for i in range(5):
    c = input("Enter a key:- ")
    a.append(c)
for j in range(5):
    d = input("Enter a value:- ")
    b.append(d)

f = tuple(a)
g = tuple(b)
e = dict(zip(f, g))
print(e)
