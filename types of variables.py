# Global Variable
college = "MIT ADT University"

class Student:
    # Class Variable
    course = "Computer Science"

    def __init__(self, name):
        # Instance Variable
        self.name = name

    def display(self):
        # Local Variable
        marks = int(input("Enter Marks: "))

        print("\n----- Student Details -----")
        print("Name:", self.name)          # Instance Variable
        print("Course:", Student.course)   # Class Variable
        print("College:", college)         # Global Variable
        print("Marks:", marks)             # Local Variable


# Main Program
name = input("Enter Student Name: ")

s1 = Student(name)
s1.display()
