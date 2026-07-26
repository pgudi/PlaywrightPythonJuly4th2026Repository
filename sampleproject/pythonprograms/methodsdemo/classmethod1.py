class BasicMaths:
    x=40
    y=30

    @classmethod
    def addition(cls):
        result=(BasicMaths.x + BasicMaths.y)
        print("Addition Result :",result)

    @classmethod
    def multiplication(cls, num1,num2):
        result= (num1 * num2)
        print("Multiplication Result :",result)

obj=BasicMaths()
obj.addition()
obj.multiplication(15,10)