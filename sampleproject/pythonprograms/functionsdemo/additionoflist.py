
def addition_list(x,y):

    if(len(x) == len(y)):
        for i in range(0, len(x)):
            print(x[i] + y[i])

list1=[1,2,3,4]
list2=[10,20,30,40]
addition_list(list1, list2)
