from abc import ABC, abstractmethod

# Abstract Class


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Child Class


class Dog(Animal):

    def sound(self):
        print("Dog barks")


# Create Object
d = Dog()
d.sound()
