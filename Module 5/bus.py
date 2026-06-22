class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def is_bus(self):
        if self.vehicle_type.lower() == "bus":
            print("Yes, this is a Bus.")
        else:
            print("No, this is not a Bus.")


vehicle = input("Enter vehicle type: ")

obj = Vehicle(vehicle)
obj.is_bus()
