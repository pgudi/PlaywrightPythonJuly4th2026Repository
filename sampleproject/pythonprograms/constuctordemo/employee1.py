class Employee:
    def __init__(self, empid=None, ename=None, jobname=None, salary=None):
        self.empid=empid
        self.ename=ename
        self.jobname=jobname
        self.salary=salary
        if(empid==None and ename==None and jobname==None and salary==None):
            print("It is a No-Args Constructor!!!")    
            print("------------------")
        elif (ename==None and jobname==None and salary==None):
            print("Employee Id :",self.empid)
            print("------------------")
        elif (jobname==None and salary==None):
            print("Employee Id :",self.empid)
            print("Employee Name :",self.ename)
            print("------------------")
        elif(salary==None):
            print("Employee Id :",self.empid)
            print("Employee Name :",self.ename)
            print("Employee Job :",self.jobname)
            print("------------------")
        else:
            print("Employee Id :",self.empid)
            print("Employee Name :",self.ename)
            print("Employee Job :",self.jobname)
            print("Employee Job :",self.salary)
            print("------------------")
        
        
        

obj1=Employee()
obj2=Employee(101)
obj3=Employee(102,"Santosh") 
obj3=Employee(103,"Bhaskar","Analyst") 
obj3=Employee(104,"Geetha","Clerk", 45000) 