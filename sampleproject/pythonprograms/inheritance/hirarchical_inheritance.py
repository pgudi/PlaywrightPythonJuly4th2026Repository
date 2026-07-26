# Hierarchical Inheritance Example
class Maths1:
    def addition(self, x, y):
        print("Addition Result :",(x + y))

class Maths2(Maths1):
   def substraction(self, x, y):
           print("Substraction Result :",(x - y)) 

class Maths3(Maths1):
    def division(self,x,y):
         print("Division Result :",(x/y))

# object of Maths2
obj1=Maths2()
obj1.substraction(40,20)
obj1.addition(50,100)

# Object of Maths3
obj2=Maths3()
obj2.division(40,10)
obj2.addition(100,400)