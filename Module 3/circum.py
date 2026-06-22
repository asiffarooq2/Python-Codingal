import math

# Function to calculate circumference


def circumference(radius):
    return 2 * math.pi * radius


# Input from user
r = float(input("Enter the radius of the circle: "))

# Function call
result = circumference(r)

print("Circumference of the circle =", round(result, 2))
