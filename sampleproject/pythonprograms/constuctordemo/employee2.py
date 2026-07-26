class Employee:
    def __init__(self, *args):
        if(len(args)==0):
            print("No Args Constructor !!!!")
            print("-----------------")
        elif(len(args)==1):
            self.empid=args[0]
            print("Employee Id :",self.empid)
            print("-----------------")
        elif(len(args)==2):
            self.empid=args[0]
            self.ename=args[1]
            print("Employee Id :",self.empid)
            print("Employee Name :",self.ename)
            print("-----------------")
        elif(len(args)==3):
            self.empid=args[0]
            self.ename=args[1]
            self.jobname=args[2]
            print("Employee Id :",self.empid)
            print("Employee Name :",self.ename)
            print("Employee JobName :",self.jobname)
            print("-----------------")
        else:
            self.empid=args[0]
            self.ename=args[1]
            self.jobname=args[2]
            self.salary=args[3]
            print("Employee Id :",self.empid)
            print("Employee Name :",self.ename)
            print("Employee JobName :",self.jobname)
            print("Employee Salary :",self.salary)
            print("-----------------")
            

o1=Employee()
o2=Employee(101)
o3=Employee(102,"Santosh")
o4=Employee(103,"Bhaskar","Analyst")
o5=Employee(104,"Srinivasa","Clerk",34000)