'''  Exercise Question 2: Write a function func1() such that it can accept a variable length of  argument and print all arguments value  '''

def prints(*a):
    for i in a:
        print(i)

prints(12, 23, 25, 35, 42, 56, 73, 84)
