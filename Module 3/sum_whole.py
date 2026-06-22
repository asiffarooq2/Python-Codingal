# Function to calculate sum of whole numbers

def sum_whole_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


# Input from user
num = int(input("Enter a whole number: "))

# Function call
result = sum_whole_numbers(num)

print("Sum of whole numbers from 0 to", num, "is", result)
