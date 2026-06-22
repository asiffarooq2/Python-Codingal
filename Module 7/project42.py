from tkinter import *


def calculate():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())

    simple_interest = (p * r * t) / 100
    compound_interest = p * ((1 + r / 100) ** t) - p

    result.delete("1.0", END)
    result.insert(END, f"Simple Interest = {simple_interest:.2f}\n")
    result.insert(END, f"Compound Interest = {compound_interest:.2f}")


root = Tk()

root.title("Interest Calculator")
root.geometry("400x400")

Label(root, text="Principal Amount").grid(row=0, column=0, padx=10, pady=10)
principal_entry = Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Rate of Interest (%)").grid(
    row=1, column=0, padx=10, pady=10)
rate_entry = Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Time Period (Years)").grid(row=2, column=0, padx=10, pady=10)
time_entry = Entry(root)
time_entry.grid(row=2, column=1, padx=10, pady=10)

Button(root, text="Calculate", command=calculate).grid(
    row=3, column=0, columnspan=2, pady=20
)

result = Text(root, height=6, width=35)
result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
