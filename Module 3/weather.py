# Function to check weather condition

def weather_condition(temp):
    if temp >= 35:
        print("It's very hot outside.")
    elif temp >= 25:
        print("The weather is pleasant.")
    elif temp >= 15:
        print("The weather is cool.")
    else:
        print("It's cold outside.")


# Taking input
temperature = float(input("Enter the temperature in °C: "))

# Function call
weather_condition(temperature)
