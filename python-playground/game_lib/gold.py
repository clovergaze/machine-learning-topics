from .category import Category


class Gold:
    def __init__(self, amount=0):
        self.name = "Gold"
        self.category = Category.OTHER
        self.amount = amount

    def calculate_weight(self):
        return self.amount / 1000

    def print(self):
        print("Name: " + self.name)
        print("Category: " + self.category.value)
        print("Amount: " + str(self.amount))
        print("Weight: " + str(self.calculate_weight()))
