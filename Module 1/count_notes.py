# Count Notes

amount = int(input("Enter the amount: "))

notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for note in notes:
    count = amount // note
    if count > 0:
        print(note, ":", count)
        amount = amount % note
