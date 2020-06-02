'''  Exercise Question 4: Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000  '''

def showemployee(name, salary="9000"):
    print("Hello! my name is", name, "I am a employee of IBM and my salary is", salary)

showemployee("Shantanu")
