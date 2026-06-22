# Diamond Pattern

rows = int(input("Enter the number of rows: "))

# Upper Half
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower Half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
