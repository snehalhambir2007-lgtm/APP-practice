class Student:
    college = "MIT ADT"

    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    @staticmethod
    def welcome():
        print("Welcome to Advanced Python")

# Main Program
Student.show_college()
Student.welcome()
