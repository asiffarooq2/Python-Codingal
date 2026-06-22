# Function to calculate due amount

def calculate_due(total_amount, paid_amount):
    return total_amount - paid_amount


# Input from user
total = float(input("Enter total bill amount: "))
paid = float(input("Enter paid amount: "))

# Function call
due = calculate_due(total, paid)

print("Due Amount =", due)
