'''  Exercise Question 3: Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string. '''


a = input("Enter a string:- ")
b = input("Enter b string:- ")
print(a[:1] + b[:1] + a[3:5] + b[3:5] + a[-3:] + b[-3:])
