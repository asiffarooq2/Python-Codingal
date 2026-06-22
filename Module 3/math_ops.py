# Mathematical Operations

def mathematical_operations(a, b):
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)

    if b != 0:
        print("Division =", a / b)
        print("Modulus =", a % b)
    else:
        print("Division and Modulus by zero are not allowed.")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

mathematical_operations(num1, num2)
