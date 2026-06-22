# Parrot Class

class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(self.name, "says: Hello!")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Create object
parrot1 = Parrot("Coco", 2)

parrot1.display()
parrot1.speak()
