# Bus Fare Calculation

class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    pass


# Create Bus Object
school_bus = Bus(50)

print("Total Bus Fare =", school_bus.fare())
