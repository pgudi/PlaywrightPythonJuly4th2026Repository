# Multi level Inheritane Example
class Maths1:
    def addition(self, x, y):
        print("Addition Result :",(x + y))

class Maths2(Maths1):
   def substraction(self, x, y):
           print("Substraction Result :",(x - y)) 

class Maths3(Maths2):
    def division(self,x,y):
         print("Division Result :",(x/y))

obj=Maths3()
obj.division(55,11)
obj.substraction(120,40)
obj.addition(80,50)