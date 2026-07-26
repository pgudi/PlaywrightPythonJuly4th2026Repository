class Employee:
    def __init__(self, empid=None, ename=None, jobname=None, salary=None):
        self.empid=empid
        self.ename=ename
        self.jobname=jobname
        self.salary=salary
        print("Employee Id :",self.empid)
        print("Employee Name :",self.ename)
        print("Employee Job :",self.jobname)
        print("Employee Salary :",self.salary)
        print("-------------------------------")


obj1=Employee()
obj2=Employee(1720)
obj3=Employee(1890,"Santosh","Manager") 