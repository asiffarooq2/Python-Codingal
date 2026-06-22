# Age Counter

def calculate_age(birth_year):
    current_year = 2026
    age = current_year - birth_year
    return age


birth_year = int(input("Enter your birth year: "))

print("Your age is:", calculate_age(birth_year), "years")
