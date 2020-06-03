'''  Exercise Question 1: Given a string of odd length greater 7, return a string made of the middle three chars of a given Stringef midremoval(): '''


a = input("Enter a string here:- ")
if len(a) % 2 == 0:
    b = int((len(a) / 2) - 3)
    c = int(b + 4)
    print(a[:b] + a[c:])
	
if len(a) % 2 == 1:
    b = int(len(a) / 2 - 1)
    c = b + 3
    print(a[:b] + a[c:])
	
midremoval()
