from tkinter import *


def check_strength():
    password = password_entry.get()
    length = len(password)

    if length <= 5:
        result_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        result_label.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        result_label.config(text="Strong", fg="light green")
    else:
        result_label.config(text="Very Strong", fg="dark green")


root = Tk()

root.title("Length Converter App")
root.geometry("400x400")

Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=20)

password_entry = Entry(root, show="*", width=25)
password_entry.pack(pady=10)

Button(
    root,
    text="Check Strength",
    command=check_strength
).pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=20)

root.mainloop()
