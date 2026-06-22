import random


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    user = input("Enter Rock, Paper, or Scissors: ").lower()

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
    elif user in choices:
        print("Computer Wins!")
    else:
        print("Invalid Choice!")


rock_paper_scissors()
