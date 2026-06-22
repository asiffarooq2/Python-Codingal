import math


def trigonometric_values(angle):
    radian = math.radians(angle)

    print("Sin =", round(math.sin(radian), 2))
    print("Cos =", round(math.cos(radian), 2))
    print("Tan =", round(math.tan(radian), 2))


angle = float(input("Enter angle in degrees: "))
trigonometric_values(angle)
