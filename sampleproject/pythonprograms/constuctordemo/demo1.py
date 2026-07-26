def show(*args):
    if(len(args)==0):
        print("No Args Constructor")
    elif(len(args)==1):
        print(args[0])


show("Welcome")

show()