def addition(x,y):
    print("Addition Result :",(x + y))

def multiplication(a, b):
    result= (a * b)
    print("Multiplication Result :",result)

def substraction(x, y):
    result=(x - y)
    print("Substraction Result :",result)

def division(a,b):
    try:
        result= (a / b)
        print("Division Result :",result)
    except ZeroDivisionError as e:
        print("Exception :",e)
    finally:
        print("This statement execute always!!")


def findFactorial(num):
    fact=1
    for i in range(1, num+1):
        fact *=i
    print("Factorial of ",num, " is ",fact)

def meanValue(x,y):
    result =(x + y)/2
    print("Mean Value :",result)

# Executing the Functions
addition(30,20)
substraction(40,10)
division(55,0)
multiplication(12,10)
findFactorial(6)
meanValue(40,50)