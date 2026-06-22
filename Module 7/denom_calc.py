from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()

root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

img = Image.open("app_img.jpg")
img = img.resize((300, 300))
photo = ImageTk.PhotoImage(img)

img_label = Label(root, image=photo, bg="light blue")
img_label.place(x=20, y=20)

label1 = Label(
    root,
    text="Welcome to the Denomination Counter",
    bg="light blue",
    font=("Arial", 14)
)
label1.place(x=20, y=330)


def topwin():
    top = Toplevel()

    top.title("Denomination Calculator")
    top.configure(bg="light green")
    top.geometry("400x300")

    def calculator():
        try:
            amount = int(entry.get())

            notes_2000 = amount // 2000
            amount %= 2000

            notes_500 = amount // 500
            amount %= 500

            notes_100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, str(notes_2000))
            t2.insert(0, str(notes_500))
            t3.insert(0, str(notes_100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    lbl_amount = Label(top, text="Enter Total Amount", bg="light green")
    entry = Entry(top)

    heading = Label(
        top,
        text="Denomination Note Count",
        bg="light green",
        font=("Arial", 12, "bold")
    )

    l1 = Label(top, text="2000", bg="light green")
    l2 = Label(top, text="500", bg="light green")
    l3 = Label(top, text="100", bg="light green")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    btn_calc = Button(
        top,
        text="Calculate",
        command=calculator,
        bg="blue",
        fg="white"
    )

    lbl_amount.place(x=30, y=30)
    entry.place(x=180, y=30)

    heading.place(x=100, y=80)

    l1.place(x=70, y=130)
    t1.place(x=180, y=130)

    l2.place(x=70, y=170)
    t2.place(x=180, y=170)

    l3.place(x=70, y=210)
    t3.place(x=180, y=210)

    btn_calc.place(x=150, y=250)

    top.mainloop()


def msg():
    response = messagebox.showinfo(
        "Confirmation",
        "Do you want to calculate denominations?"
    )

    if response == "ok":
        topwin()


button1 = Button(
    root,
    text="Let's get started!",
    command=msg,
    bg="blue",
    fg="white"
)

button1.place(x=250, y=360)

root.mainloop()
