from tkinter import *

root = Tk()

root.title("Login App")
root.geometry("400x400")

frame = Frame(root, height=250, width=350, bg="lightblue")

name_label = Label(frame, text="Full Name",
                   bg="lightblue", fg="black", width=12)
email_label = Label(frame, text="Email Id",
                    bg="lightblue", fg="black", width=12)
pass_label = Label(frame, text="Password",
                   bg="lightblue", fg="black", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")


def display():
    name = name_entry.get()

    greeting = f"Hello, {name}!\n"
    message = "Your account has been created successfully.\n\n"

    textbox.insert(END, greeting)
    textbox.insert(END, message)


textbox = Text(root, height=6, width=40)

btn = Button(
    frame,
    text="Create Account",
    command=display,
    bg="lightgreen"
)

frame.place(x=25, y=20)

name_label.place(x=20, y=20)
name_entry.place(x=140, y=20)

email_label.place(x=20, y=70)
email_entry.place(x=140, y=70)

pass_label.place(x=20, y=120)
pass_entry.place(x=140, y=120)

btn.place(x=120, y=180)

textbox.place(x=40, y=290)

root.mainloop()
