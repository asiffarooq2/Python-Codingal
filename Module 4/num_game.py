import random


def guess_the_number():
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret_number:
            print("Too Low! Try Again.")
        elif guess > secret_number:
            print("Too High! Try Again.")
        else:
            print("Congratulations! You guessed the number.")
            break


guess_the_number()
