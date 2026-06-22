from tkinter import *

root = Tk()

root.title("Number Pad")
root.geometry("250x300")

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]

for i in range(4):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

    for j in range(3):
        frame = Frame(root, relief=SUNKEN, borderwidth=1)
        frame.grid(row=i, column=j, sticky="nsew")

        label = Label(
            frame,
            text=str(nums[i][j]),
            bg="lightblue"
        )
        label.pack(padx=20, pady=20)

root.mainloop()
