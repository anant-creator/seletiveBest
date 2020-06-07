''' Exercise Question 8: Find all occurrences of “USA” in given string ignoring the case '''

a = input("Enter a string:- ")
b = a.count("usa")
c = a.count("USA")
d = b + c
print("The occurance of usa in input string is %d" % (d))
