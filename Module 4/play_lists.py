# Play with Lists

def play_with_lists():
    fruits = ["Apple", "Banana", "Mango"]

    print("Original List:", fruits)

    # Add an item
    fruits.append("Orange")
    print("After Append:", fruits)

    # Remove an item
    fruits.remove("Banana")
    print("After Remove:", fruits)

    # Access an item
    print("First Fruit:", fruits[0])

    # Length of list
    print("Number of Fruits:", len(fruits))


play_with_lists()
