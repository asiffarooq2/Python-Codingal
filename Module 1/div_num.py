# Check if a number is divisible by another number

num = int(input("Enter a number: "))
divisor = int(input("Enter the divisor: "))

if num % divisor == 0:
    print(num, "is divisible by", divisor)
else:
    print(num, "is not divisible by", divisor)
