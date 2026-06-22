from tkinter import *


def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2

    result_box.delete("1.0", END)
    result_box.insert(END, f"Product = {product}")


root = Tk()

root.title("Getting Started with Widgets")
root.geometry("400x300")

label = Label(
    root, text="Enter two numbers and click the button to calculate their product.")
label.pack(pady=10)

label1 = Label(root, text="Enter First Number:")
label1.pack()

entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Enter Second Number:")
label2.pack()

entry2 = Entry(root)
entry2.pack()

button = Button(root, text="Calculate Product", command=calculate_product)
button.pack(pady=10)

result_box = Text(root, height=3, width=30)
result_box.pack()

root.mainloop()
