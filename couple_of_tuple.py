''' Exercise Question 5: Given a two list of equal size create a set such that it shows the element from both lists in the pair '''

first = [12, 36, 49, 98, 45, 67, 43]
second = [34, 67, 74, 87, 76, 33, 65]

ret = tuple(zip(first, second))
sup_ret = set(ret)
print(sup_ret)


