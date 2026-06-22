# Dog Class

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display(self):
        print("Dog Name:", self.name)
        print("Dog Breed:", self.breed)


# Create object
dog1 = Dog("Buddy", "Labrador")

dog1.display()
