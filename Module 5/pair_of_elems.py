# Pair of Elements

class PairElements:
    def __init__(self, elements):
        self.elements = elements

    def display_pairs(self):
        for i in range(len(self.elements)):
            for j in range(i + 1, len(self.elements)):
                print(self.elements[i], self.elements[j])


# User Input
numbers = [1, 2, 3, 4]

obj = PairElements(numbers)
obj.display_pairs()
