from b import *


def multiplyNumbers(a, b):
    multiply(a,b)
 
def divideNumbers(a, b):
    print("Division is ", a / b)
 
def modulusNumbers(a, b):
    print("Remainder is ", a % b)
	

if __name__=="__main__":
    var1=sys.argv[1]
    var2=sys.argv[2]
    subtractNumbers(var1,var2)