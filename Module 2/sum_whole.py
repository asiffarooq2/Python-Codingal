# Sum of Whole Numbers from 0 to n

n = int(input("Enter a whole number: "))

total = 0

for i in range(n + 1):
    total += i

print("Sum of whole numbers from 0 to", n, "is", total)
