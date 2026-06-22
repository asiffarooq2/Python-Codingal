# Function to print numbers except 5

def print_numbers():
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)


# Function call
print_numbers()
