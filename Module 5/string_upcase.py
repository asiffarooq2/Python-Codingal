# String Uppercase Using Classes

class StringOperations:
    def __init__(self, text):
        self.text = text

    def to_uppercase(self):
        print("Uppercase String:", self.text.upper())


# User Input
text = input("Enter a string: ")

# Create Object
obj = StringOperations(text)

# Call Method
obj.to_uppercase()
