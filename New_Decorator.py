''' decorator for smart output '''
def multi(a, b):
    Pass
	
def check(func):
	
    def joy(a, b):
        if (a**b) > 1000:
	    print(a+b)
	elif (a**b) < 1000:
	    print(a**b)
	
    return joy
	
multi = check(multi)
multi(3, 3)
