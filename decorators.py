# Function Decorator
def uppercase(func):
    def wrapper(*args):
        return func(*args).upper()
    return wrapper

class Student:
    college = "MIT ADT"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    @staticmethod
    def welcome():
        print("Welcome to Python")

    @uppercase
    def display(self):
        return f"Student Name: {self.name}"


# Main Program
name = input("Enter Student Name: ")

s = Student(name)

print(s.display())
Student.show_college()
Student.welcome()
