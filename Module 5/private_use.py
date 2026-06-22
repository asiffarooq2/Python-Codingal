# Private Variable Example

class Student:
    def __init__(self):
        self.__marks = 95   # Private variable

    def display(self):
        print("Marks:", self.__marks)


obj = Student()

obj.display()
