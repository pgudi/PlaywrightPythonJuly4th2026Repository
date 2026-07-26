class Maths1:
    def addition(self, x, y):
        print("Addition Result :",(x + y))

class Maths2:
   def substraction(self, x, y):
           print("Substraction Result :",(x - y)) 

class Maths3(Maths1, Maths2):
    def division(self,x,y):
         print("Division Result :",(x/y))

# object for Maths3
obj=Maths3()
obj.division(120,10)
obj.substraction(50,25)
obj.addition(110,50)