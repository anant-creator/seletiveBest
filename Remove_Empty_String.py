''' Exercise Question 6: Remove empty strings from the list of strings '''

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i in list1:
    if len(i) < 1:
        list1.remove(i)

print(list1)
