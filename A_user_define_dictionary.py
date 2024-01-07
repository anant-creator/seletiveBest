'''  Exercise - create a user input array and then create a dictionary from it ''' 

a = []
b = []

def dictionaryAdd:
    c = input("Enter a key:- ")
    a.append(c)
    d = input("Enter a value:- ")
    b.append(d)
    f = tuple(a)
    g = tuple(b)
    e = dict(zip(f, g))
    print(e)
    dictionaryAdd()
    

dictionaryAdd()
