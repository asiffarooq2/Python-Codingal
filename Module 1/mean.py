# Mean Value Calculator

n = int(input("Enter the number of values: "))

total = 0

for i in range(n):
    num = float(input("Enter a number: "))
    total += num

mean = total / n

print("Mean =", mean)
