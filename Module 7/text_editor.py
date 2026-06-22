from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    txt_edit.delete(1.0, END)

    with open(filepath, "r") as file:
        text = file.read()

    txt_edit.insert(END, text)
    window.title(f"Codingal's Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "w") as file:
        text = txt_edit.get(1.0, END)
        file.write(text)

    window.title(f"Codingal's Text Editor - {filepath}")


window = Tk()

window.title("Codingal's Text Editor")
window.geometry("600x500")

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

txt_edit = Text(window)

fr_buttons = Frame(window)

btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.pack(fill=X, padx=5, pady=5)
btn_save.pack(fill=X, padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
