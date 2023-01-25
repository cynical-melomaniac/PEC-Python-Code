class Student:
    pass
class Marks:
    pass

student1 = Student()
student2 = Student()
student3 = Student()

marks1 = Marks()
marks2 = Marks()
marks3 = Marks()

if isinstance(student1, Student):
    print("Student1 is an instance of class Student.")
if isinstance(student2, Student):
    print("Student2 is an instance of class Student.")
if isinstance(student3, Student):
    print("Student3 is an instance of class Student.")

if isinstance(marks1, Marks):
    print("marks1 is an instance of class Student.")
if isinstance(marks2, Marks):
    print("marks2 is an instance of class Student.")
if isinstance(marks3, Marks):
    print("marks3 is an instance of class Student.")
    
if issubclass(type(Student), type(type)):
    print("Student is a subclass of class.")
if issubclass(type(Marks), type(type)):
    print("Marks is a subclass of class.")