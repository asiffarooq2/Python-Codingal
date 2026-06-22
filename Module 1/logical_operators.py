# AND and OR Operators

age = int(input("Enter your age: "))
has_id = input("Do you have an ID card? (yes/no): ")

# AND Operator
if age >= 18 and has_id.lower() == "yes":
    print("You are allowed to vote.")
else:
    print("You are not allowed to vote.")

# OR Operator
if age >= 18 or has_id.lower() == "yes":
    print("At least one condition is True.")
else:
    print("Both conditions are False.")
