class Multiply:
    def multiplication(self, *args):
        if(len(args)==0):
            print("This Method should perform Multipication Action!!")
        elif(len(args)==1):
            print("Multiplication Result :",args[0] * 1)
        elif(len(args)==2):
            print("Multiplication Result :",(args[0] * args[1]))
        elif(len(args)==3):
            print("Multiplication Result :",(args[0] * args[1] * args[2]))
        elif(len(args)==4):
            print("Multiplication Result :",(args[0] * args[1] * args[2] * args[3]))
        else:
            print("Multiplication Result :",(args[0] * args[1] * args[2] * args[3] * args[4]))


obj=Multiply()
obj.multiplication()
obj.multiplication(45)
obj.multiplication(15,10)
obj.multiplication(10,3,5)