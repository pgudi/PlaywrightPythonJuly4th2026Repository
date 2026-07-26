class Employee:
    def __init__(self, empid,ename,job,sal,department):
        self.empid=empid
        self.ename=ename
        self.job=job
        self.sal=sal
        department.show_department_details()

    def display_employee_details(self):
        print("Employee Id :",self.empid)
        print("Employee Name :",self.ename)
        print("Employee Job :",self.job)
        print("Employee Salary :",self.sal)

    class Department:
        def __init__(self, deptno,dname,loc):
            self.deptno=deptno
            self.dname=dname
            self.loc=loc

        def show_department_details(self):
            print("Department Id :",self.deptno)
            print("Department Name :",self.dname)
            print("Department Location :",self.loc)

dept=Employee.Department(10,"Accounting","Boston")
emp=Employee(101,"Santosh","Manager",47000,dept)
emp.display_employee_details()