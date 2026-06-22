# Flip-Flop: Swap Two Numbers

def flip_flop(a, b):
    a, b = b, a

    print("After Swapping:")
    print("First Number =", a)
    print("Second Number =", b)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

flip_flop(num1, num2)
