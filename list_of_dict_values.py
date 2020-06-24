''' Exercise Question 9: Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates '''


speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
deed = []
for i in speed.values():
        deed.append(i)

print(list(set(deed)))
