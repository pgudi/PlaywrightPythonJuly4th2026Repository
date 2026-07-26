class Employee:
    location = "CALIFORNIA"
    def __init__(self, eno, ename, job, sal):
        self.empno=eno
        self.empname=ename
        self.jobname=job
        self.salary=sal



obj1=Employee(101,"Adams","Clerk",12000)
print(obj1.empno)
print(obj1.empname)
print(obj1.jobname)
print(obj1.salary)
print(Employee.location)

print("------------")

obj2=Employee(102,"Jones","Analyst", 13000)
print(obj2.empno)
print(obj2.empname)
print(obj2.jobname)
print(obj2.salary)
print(Employee.location)