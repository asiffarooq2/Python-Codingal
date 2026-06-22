from tkinter import *
from tkinter import messagebox
from datetime import date


def greet():
    name = entry.get()

    if name:
        today = date.today().strftime("%d-%m-%Y")
        text_box.delete("1.0", END)
        text_box.insert(END, f"Hello, {name}!\n")
        text_box.insert(END, f"Today's Date: {today}")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")


root = Tk()
root.title("Greeting Application")
root.geometry("400x300")

Label(root, text="Enter Your Name:").pack(pady=10)

entry = Entry(root, width=30)
entry.pack(pady=5)

Button(root, text="Greet Me", command=greet).pack(pady=10)

text_box = Text(root, height=5, width=35)
text_box.pack(pady=10)

root.mainloop()
