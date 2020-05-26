''' Question 3: Accept string from a user and display only those characters which are present at an even index number. '''

i = 0
a = input("Enter a string:- ")
while i < len(a):
    print(i, a[i])
    i += 2
