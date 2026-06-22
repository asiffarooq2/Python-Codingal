# Check Frequency of an Element

def check_frequency():
    numbers = [1, 2, 2, 3, 4, 2, 5, 3]

    element = int(input("Enter the element to find: "))

    frequency = numbers.count(element)

    print("Frequency of", element, "=", frequency)


check_frequency()
