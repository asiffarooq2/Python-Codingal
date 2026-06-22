# Tuple Product

def tuple_product(numbers):
    product = 1

    for num in numbers:
        product *= num

    return product


nums = (2, 3, 4, 5)

print("Tuple:", nums)
print("Product =", tuple_product(nums))
