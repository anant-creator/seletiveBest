''' Exercise Question 8: Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list '''


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
S = ["h", "i", "j"]
list1[2][1][2].extend(S)
print(list1)
