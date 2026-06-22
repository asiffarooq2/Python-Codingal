# Trip Expenditure Calculator

def calculate_trip_expense(travel, hotel, food, shopping):
    return travel + hotel + food + shopping


travel = float(input("Enter travel expense: "))
hotel = float(input("Enter hotel expense: "))
food = float(input("Enter food expense: "))
shopping = float(input("Enter shopping expense: "))

total = calculate_trip_expense(travel, hotel, food, shopping)

print("Total Trip Expenditure =", total)
