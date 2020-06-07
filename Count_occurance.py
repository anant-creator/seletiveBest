''' Exercise Question 10: Given an input string, count occurrences of all characters within a string '''


listt = []
def string(n):
	global listt
	for i in n:
		a = n.count(i)
		if i not in listt:
			listt.append(i)
			listt.append(a)
		
	print(listt)
		
string("gravess")
