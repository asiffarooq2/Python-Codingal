from tkinter import *
import random


def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"Your Choice: {user_choice}\n"
        f"Computer Choice: {computer_choice}\n"
        f"Result: {result}"
    )


root = Tk()

root.title("Length Converter App")
root.geometry("400x400")

heading = Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 16, "bold")
)
heading.pack(pady=20)

Button(
    root,
    text="Rock",
    width=15,
    command=lambda: play("Rock")
).pack(pady=5)

Button(
    root,
    text="Paper",
    width=15,
    command=lambda: play("Paper")
).pack(pady=5)

Button(
    root,
    text="Scissors",
    width=15,
    command=lambda: play("Scissors")
).pack(pady=5)

result_label = Label(
    root,
    text="Choose an option to start!",
    font=("Arial", 12)
)
result_label.pack(pady=30)

root.mainloop()
