# Simple Inheritance Example
class Maths1:
    def addition(self, x, y):
        print("Addition Result :",(x + y))

class Maths2(Maths1):
   def substraction(self, x, y):
           print("Substraction Result :",(x - y)) 

obj=Maths2()
obj.substraction(440,10)
obj.addition(40,50)