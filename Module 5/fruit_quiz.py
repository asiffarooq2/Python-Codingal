# Fruit Quiz

class FruitQuiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_question(self):
        user_answer = input(self.question + " ")

        if user_answer.lower() == self.answer.lower():
            print("Correct! ✅")
        else:
            print("Wrong! ❌")
            print("Correct Answer:", self.answer)


# Create Quiz Questions
q1 = FruitQuiz("Which fruit is yellow and loved by monkeys?", "Banana")
q2 = FruitQuiz("Which fruit keeps the doctor away?", "Apple")
q3 = FruitQuiz("Which fruit is known as the king of fruits?", "Mango")

# Start Quiz
q1.ask_question()
q2.ask_question()
q3.ask_question()
