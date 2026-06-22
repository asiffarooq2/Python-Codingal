# Vehicle Polymorphism

class Car:
    def move(self):
        print("Car is driving 🚗")


class Bike:
    def move(self):
        print("Bike is riding 🏍️")


class Bus:
    def move(self):
        print("Bus is moving 🚍")


# Polymorphism
vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.move()
