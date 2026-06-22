# Word Matching

def word_match():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    if word1.lower() == word2.lower():
        print("Words Match!")
    else:
        print("Words Do Not Match!")


word_match()
