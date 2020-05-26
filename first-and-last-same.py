''' Question 5: Given a list of numbers, return True if first and last number of a list is same '''

a = []
while True:
    b = input("Enter a list element:- ")
    a.append(b)
    print(a)
    if a[0] == a[-1]:
        print("True")
    else:
        print("False")
