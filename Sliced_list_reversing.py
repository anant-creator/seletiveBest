''' Exercise Question 3: Given a list slice it into a 3 equal chunks and reverse each list '''


list = [12,13,14,15,16,17,18,19,20]
a =  list[:3]; b = list[3:6]; c = list[6:9]
			
print(a)
a.reverse()
print("reversed", a)
print(b)
b.reverse()
print("reversed", a)
print(c)
c.reverse()
print("reversed", a)
