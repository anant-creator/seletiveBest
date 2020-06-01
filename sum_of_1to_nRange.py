''' Exercise Question 3: Accept n number from user and calculate the sum of all number between 1 and n including  '''


#sum of range
total = 0
def sum(n):
    global total
    for i in range(n):
        total += i
    print(total)

sum(12)
