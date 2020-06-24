''' dictionary exercise 2: Merge following two Python dictionaries into one '''


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

a = list(dict1.keys())
b = list(dict2.keys())
c = list(dict1.values())
d = list(dict2.values())
e = a + b
f = c + d
print(dict(zip(e, f)))
