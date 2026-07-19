
def add(x,y):
    return (x + y)

def sub1(a,b):
    result=(a - b)
    return result

def multiplication(p, q):
    result= (p * q)
    print("Multiplication Result :",result)

# First Appraoch
v1= add(10,5)
v2=sub1(35,25)

multiplication(v1,v2)

# Second Approach
multiplication(add(5,4), sub1(15,5))
