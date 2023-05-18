from c import *


def subtractNumbers(a, b):
    print("Difference is ", a-b)
    
def multiply(a, b):
    print("Product is ", a * b)
	

if __name__=="__main__":
    var1=sys.argv[1]
    var2=sys.argv[2]
    addNumbers(var1,var2)