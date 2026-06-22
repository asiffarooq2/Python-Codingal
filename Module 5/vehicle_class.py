# Vehicle Class

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Create object
vehicle1 = Vehicle("Toyota", "Fortuner")

# Display details
vehicle1.display()
