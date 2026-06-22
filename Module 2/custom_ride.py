# Customize Your Ride

print("Welcome to Car Customization!")

car_model = input("Enter Car Model: ")

print("\nChoose Color:")
print("1. Red")
print("2. Blue")
print("3. Black")
color_choice = int(input("Enter choice (1-3): "))

if color_choice == 1:
    color = "Red"
elif color_choice == 2:
    color = "Blue"
else:
    color = "Black"

print("\nChoose Engine:")
print("1. Petrol")
print("2. Diesel")
print("3. Electric")
engine_choice = int(input("Enter choice (1-3): "))

if engine_choice == 1:
    engine = "Petrol"
elif engine_choice == 2:
    engine = "Diesel"
else:
    engine = "Electric"

print("\n--- Your Customized Ride ---")
print("Car Model:", car_model)
print("Color:", color)
print("Engine:", engine)
print("Thank you for customizing your ride!")
