''' Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string '''
a = input("Enter a string:- ")
b = int(input("Enter a number to remove alphabets till that num.:- "))
print(a[b+1:])
