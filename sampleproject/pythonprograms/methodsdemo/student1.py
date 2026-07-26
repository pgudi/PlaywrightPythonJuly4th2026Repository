class Student:
    def __init__(self, rollno, firstname, course):
        self.rollno=rollno
        self.firstname=firstname
        self.course=course

    def showRollNumber(self):
        print("Roll Number :",self.rollno)

    def showFirstName(self):
        print("First Name of Student :",self.firstname)

    def showCourseName(self):
        print("Course Name :",self.course)

obj=Student(10, "Santosh","Science")
obj.showRollNumber()
obj.showFirstName()
obj.showCourseName()

        