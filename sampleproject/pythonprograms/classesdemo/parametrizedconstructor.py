class Department:
    def __init__(self, deptno, dname,loc):
        self.deptno=deptno
        self.dname=dname
        self.loc=loc


obj=Department(10, "Accounting", "Dallas")
print(obj.deptno)
print(obj.dname)
print(obj.loc)

obj2=Department(20,"Research", "Boston")
print(obj2.deptno)
print(obj2.dname)
print(obj2.loc)