''' create a function to remove all vowel elements from the input string '''

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
a = input("Enter a string here:- ")
c = " "
for j in a:
    if j not in vowels:
                c += j
            
print(c)
