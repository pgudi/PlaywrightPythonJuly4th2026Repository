class Outer:
    def showFirstName(self,fname):
        print("First Name :",fname)

    def showJobName(self, jobname):
        print("Job Name :",jobname)

    class Inner:
        def __init__(self):
            Outer.showFirstName(self,"Santosh")
            Outer.showJobName(self, "Sales Manager")

        def displayLocation(self, loc):
            print("Location :",loc)


obj=Outer()
obj.Inner().displayLocation("New York")

