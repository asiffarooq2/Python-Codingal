# All About Countries

class Country:
    def __init__(self, name, capital, currency):
        self.name = name
        self.capital = capital
        self.currency = currency

    def display(self):
        print("Country:", self.name)
        print("Capital:", self.capital)
        print("Currency:", self.currency)


# Create Object
country1 = Country("India", "New Delhi", "Indian Rupee")

country1.display()
