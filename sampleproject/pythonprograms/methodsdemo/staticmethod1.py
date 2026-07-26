class BasicMaths:
    x=40

    @staticmethod
    def addition(y):
        result= (BasicMaths.x + y)
        print("Addition Result :",result)


obj=BasicMaths()
obj.addition(30)