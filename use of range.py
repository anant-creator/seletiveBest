''' Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current
number and previous number '''

cn = 0
pn = 0
sum = 0
 
for cn in range(10):
    print("Current Number: ", cn, "Previous Number: ", pn, "Sum of both: ", sum)
    cn += 1 
    pn = (cn - 1)
    sum = pn + cn



while cn < 10:
    print("Current Number: ", cn, "Previous Number: ", pn, "Sum of both: ", sum)
    cn += 1
    pn = (cn - 1)
    sum = pn + cn

