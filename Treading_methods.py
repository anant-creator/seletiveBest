'''  Create two classes and run them on different threads properly  '''


from threading import *
import time

class manu(Thread):
    def run(self):
        for i in range(500):
	    time.sleep(1)
	    print("            We all care for each other  ")
	    print(" ")
			
class tanu(Thread):
    def run(self):
        for i in range(500):
	    time.sleep(1)
	        print("Please help! Mahadev Save us from all problems")
		print(" ")
			
a1 = manu()
a2 = tanu()

a1.start()
time.sleep(0.3)
a2.start()
		
a1.join()
a2.join()

print("She deserves your mercy")
