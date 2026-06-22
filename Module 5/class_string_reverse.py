# String Reverse Using Classes

class ReverseString:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        print("Reversed String:", self.text[::-1])


# User Input
text = input("Enter a string: ")

# Create Object
obj = ReverseString(text)

# Call Method
obj.reverse()
