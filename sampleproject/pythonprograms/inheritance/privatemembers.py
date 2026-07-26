class Employee:
    def __init__(self, ename, jobname):
        self._ename=ename
        self._jobname=jobname

class Department(Employee):
    def __init__(self, dname, ename,job):
        super().__init__(ename,job)
        self.dname=dname

obj=Department("Research", "Santosh","Analyst")
print(obj.dname)
print(obj.ename)
print(obj.jobname)
