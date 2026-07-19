
def outer_func():
    outer_x=100
    def inner_func():
        inner_y=200
        print("inner_y :",inner_y)
        print("outer_x :",outer_x)
    inner_func()
    
    print("outer_x :",outer_x)
    #print("inner_y :",inner_y)  can't access

outer_func()

