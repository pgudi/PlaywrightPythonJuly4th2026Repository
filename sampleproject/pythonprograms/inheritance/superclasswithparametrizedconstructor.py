class Student:
    def __init__(self, firstname, coursename):
        self.firstname=firstname
        self.coursename=coursename

    def show_student_Details(self):
        print("Student Name :",self.firstname)
        print("Course Name :",self.coursename)

class Library(Student):
    def __init__(self, fistname, coursename, bookname):
        super().__init__(fistname, coursename)
        self.bookname=bookname

    def show_book_details(self):
        print("Book Name :",self.bookname)

obj=Library("Santosh","Science","Chemistry")
obj.show_book_details()
obj.show_student_Details()