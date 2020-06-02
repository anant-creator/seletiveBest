'''  Exercise Question 3: Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call '''

def calculator():
    a = int(input("Enter a Number:- "))
    b = input("Enter a operator:- ")
    c = int(input("Enter b number:- "))
    if b == "+":
        print(a + c)
    if b == "-":
        if (a < c):
            a, c = c, a
            print(a - c)
        
calculator()
