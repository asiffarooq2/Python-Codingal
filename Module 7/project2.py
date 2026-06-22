from tkinter import *
from datetime import date


def calculate_age():
    name = name_entry.get()
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()

    age = today.year - year

    if (today.month, today.day) < (month, day):
        age -= 1

    result.delete("1.0", END)
    result.insert(
        END,
        f"Hello {name}!\nYou are {age} years old."
    )


root = Tk()

root.title("Age Calculator App")
root.geometry("400x400")

Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky=W)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Date").grid(row=1, column=0, padx=10, pady=10, sticky=W)
day_entry = Entry(root)
day_entry.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Month").grid(row=2, column=0, padx=10, pady=10, sticky=W)
month_entry = Entry(root)
month_entry.grid(row=2, column=1, padx=10, pady=10)

Label(root, text="Year").grid(row=3, column=0, padx=10, pady=10, sticky=W)
year_entry = Entry(root)
year_entry.grid(row=3, column=1, padx=10, pady=10)

Button(root, text="Calculate Age", command=calculate_age).grid(
    row=4, column=0, columnspan=2, pady=20
)

result = Text(root, height=5, width=35)
result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
