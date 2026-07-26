# Hybrid Inheritance Example

class Maths1:
    def addition(self, x, y):
        print("Addition Result :",(x + y))

class Maths2(Maths1):
   def substraction(self, x, y):
           print("Substraction Result :",(x - y)) 

class Maths3(Maths1):
    def division(self,x,y):
         print("Division Result :",(x/y))

class Maths4(Maths3):
     def multiplication(self, x, y):
          print("Multilpication Result:",(x * y))

# Object for Maths2
obj1=Maths2()
obj1.substraction(50,20)
obj1.addition(50,60)

# Object fro Maths4
obj2=Maths4()
obj2.multiplication(14,10)
obj2.division(100,10)
obj2.addition(35,100)