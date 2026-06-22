# Sets Example
# Remove Duplicates Using Sets

def remove_duplicates(numbers):
    unique_numbers = set(numbers)
    return unique_numbers


numbers = [1, 2, 2, 3, 4, 4, 5, 5]

print("Original List:", numbers)
print("After Removing Duplicates:", remove_duplicates(numbers))
