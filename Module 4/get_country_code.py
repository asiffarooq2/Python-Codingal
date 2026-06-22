# Get Country Code

def get_country_code(country):
    country_codes = {
        "India": "+91",
        "USA": "+1",
        "UK": "+44",
        "Canada": "+1",
        "Australia": "+61"
    }

    return country_codes.get(country, "Country not found")


country = input("Enter country name: ")

print("Country Code:", get_country_code(country))
