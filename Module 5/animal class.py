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

# Child Class


class Cat(Animal):

    def sound(self):
        print("Cat meows")


# Create Objects
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
