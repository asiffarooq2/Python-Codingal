# Function to calculate cube

def cube(num):
    return num ** 3


# Input from user
number = int(input("Enter a number: "))

# Function call
result = cube(number)

print("Cube of", number, "is", result)
