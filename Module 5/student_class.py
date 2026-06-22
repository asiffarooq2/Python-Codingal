# Student Class

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


# Create object
student1 = Student("Asif", 16, "A")

# Display details
student1.display()
