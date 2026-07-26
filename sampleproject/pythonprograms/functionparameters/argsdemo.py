def sumOfNumbers(*args):
    sum=0
    for i in args:
        sum=sum + i
    print("Sum of Elements :",sum)

sumOfNumbers(10,20)
sumOfNumbers(10,20,30)
sumOfNumbers(10,20,30,40)
sumOfNumbers(10,20,30,40,50)
sumOfNumbers(1,2,3,4,5,6,7,8,9,10)