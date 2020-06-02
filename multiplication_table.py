''' Exercise Question 4: Accept n number from user and print its multiplication table '''

#sum of range
total = 0
def sum(n):
    global total
    for i in range(n):
        total += i
        print(total)

sum(12)
