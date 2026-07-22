class Student:
    college = "MIT ADT"

    def __init__(self, name):
        self.name = name

    # Instance Method
    def display(self):
        print("Name:", self.name)

    # Class Method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static Method
    @staticmethod
    def welcome():
        print("Welcome!")

# Main Program
name = input("Enter Name: ")

s = Student(name)
s.display()
Student.show_college()
Student.welcome()
