''' Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list
and even numbers from the second list '''

a = [10, 20, 30, 40, 50, 23, 27, 33]
b = [37, 27, 73, 12, 22, 26, 20, 30]
c = []

for i in range(len(a)):
    if a[i] % 2 != 0:
        c.append(a[i])
for f in range(len(b)):
    if b[f] % 2 == 0:
        c.append(b[f])

print(c)
