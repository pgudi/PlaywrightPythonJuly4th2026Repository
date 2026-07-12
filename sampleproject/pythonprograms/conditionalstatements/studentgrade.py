marks=72600

if( marks>=70 and marks<=100):
    print("Result is First class with Distinction!!!!")
elif(marks<70 and marks>=60):
    print("Result is First class!!!")
elif(marks<60 and marks>=50):
    print("Result is Second class!!!")
elif(marks<50 and marks>=35):
    print("Result is Pass class!!!")
elif(marks<35 and marks>=0):
    print("Result has failed!!!")
else:
    print("The Given Marks is Invalid!!")