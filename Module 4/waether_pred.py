# Weather Prediction Using Functions

def weather_prediction(temperature):
    if temperature >= 35:
        print("Prediction: Hot Day")
    elif temperature >= 25:
        print("Prediction: Pleasant Weather")
    elif temperature >= 15:
        print("Prediction: Cool Weather")
    else:
        print("Prediction: Cold Weather")


temp = float(input("Enter the temperature (°C): "))

weather_prediction(temp)
