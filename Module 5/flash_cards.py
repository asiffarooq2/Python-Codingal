# Flashcards Quiz

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def quiz(self):
        user_answer = input(self.question + " ")

        if user_answer.lower() == self.answer.lower():
            print("Correct! ✅")
        else:
            print("Wrong! ❌")
            print("Correct Answer:", self.answer)


# Create Flashcards
card1 = Flashcard("What is the capital of India?", "New Delhi")
card2 = Flashcard("What is 5 + 3?", "8")
card3 = Flashcard("Which language is used for AI and Data Science?", "Python")

# Start Quiz
card1.quiz()
card2.quiz()
card3.quiz()
