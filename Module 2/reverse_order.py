# Reverse Order

n = int(input("Enter a number: "))

while n > 0:
    digit = n % 10
    print(digit, end="")
    n = n // 10
