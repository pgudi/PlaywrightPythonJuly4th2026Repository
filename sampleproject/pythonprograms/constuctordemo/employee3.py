class Employee:
    def __init__(self, **kwargs):
        if(kwargs.get("empid")==None and kwargs.get("ename")==None and kwargs.get("job")==None and kwargs.get("sal")==None):
            print("No - Args Constructor !!!!")
            print("-------------------")
        elif(kwargs.get("ename")==None and kwargs.get("job")==None and kwargs.get("sal")==None):
            print("employee Id :",kwargs.get("empid"))
            print("-------------------")
        elif(kwargs.get("job")==None and kwargs.get("sal")==None):
            print("employee Id :",kwargs.get("empid"))
            print("Employee Name :",kwargs.get("ename"))
            print("-------------------")
        elif(kwargs.get("sal")==None):
            print("employee Id :",kwargs.get("empid"))
            print("Employee Name :",kwargs.get("ename"))
            print("Employee Job :",kwargs.get("job"))
            print("-------------------")
        else:
            print("employee Id :",kwargs.get("empid"))
            print("Employee Name :",kwargs.get("ename"))
            print("Employee Job :",kwargs.get("job"))
            print("Employee Salary:",kwargs.get("sal"))
            print("-------------------")

        


o1=Employee()
o2=Employee(empid=101)
o3=Employee(empid=102, ename="Santosh")
o3=Employee(empid=102, ename="Santosh", job="Sales Manager")
o4=Employee(empid=102, ename="Santosh",job="Sales Manager", sal=45000)