from tkinter import *


def convert():
    meters = float(entry.get())
    centimeters = meters * 100

    result.delete("1.0", END)
    result.insert(END, f"{meters} meters = {centimeters} centimeters")


root = Tk()

root.title("Length Converter App")
root.geometry("400x400")

Label(root, text="Length Converter", font=("Arial", 16)).pack(pady=10)

Label(root, text="Enter Length in Meters:").pack(pady=5)

entry = Entry(root, width=20)
entry.pack(pady=5)

Button(root, text="Convert", command=convert).pack(pady=10)

result = Text(root, height=5, width=35)
result.pack(pady=10)

root.mainloop()
