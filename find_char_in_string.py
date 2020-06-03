''' Find desired character in input string and also find the numbers of vowels in it '''

vowels = ["a", "e", "i", "o", "u"]
c = 0; v = 0
a = input("Enter a string here:- ")
b = input("Enter a keyword to find:- ")
for j in a:
    if b == j or b.upper() == j:
            c += 1
    for k in vowels:
        if k == j or k.upper() == j:
            v += 1
        
print("The number of desired characters in string is", c, ", The count of vowels in the sitring is ", v,".")


