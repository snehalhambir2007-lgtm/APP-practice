class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

# Main Program
name = input("Enter Student Name: ")

s = Student(name)   # Object Creation
s.display()
