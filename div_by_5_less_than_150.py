''' Exercise Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration '''

last = [10, 25, 32, 45, 52, 60, 74, 87, 90, 298, 110, 123, 245]
for i in last:
    if i%5==0 and i < 150:
        print(i)
