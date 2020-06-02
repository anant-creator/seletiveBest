'''  Exercise Question 5: Create an inner function to calculate the addition in outhe following way  '''


def outer(a, b):
    print("Result is:-")
    
    def inner(a, b):
        return a+b
    add = inner(a, b)
    return add+5
    
result = outer(5, 9)
print(result)
    
