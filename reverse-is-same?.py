''' Question 9: Reverse a given number and return true if it is the same as the original number '''

b = ""
a = input("Enter a number to flip:- ")
for i in range(len(a)):
    b += a[-1::-1]
    print(b)
    break

if a == b:
    print(True)
else:
    print(False)
