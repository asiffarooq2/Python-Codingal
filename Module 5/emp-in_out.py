# Employee In and Out Using Classes

class Employee:
    def __init__(self, name):
        self.name = name

    def check_in(self):
        print(self.name, "has checked in.")

    def check_out(self):
        print(self.name, "has checked out.")


# User Input
name = input("Enter employee name: ")

# Create Object
emp = Employee(name)

# Employee Actions
emp.check_in()
emp.check_out()
