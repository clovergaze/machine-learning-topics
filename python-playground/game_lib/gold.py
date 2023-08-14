from .category import Category


class Gold:
    @staticmethod
    def _validate_amount_is_positive(amount):
        if amount < 0:
            raise ValueError("Amount must be positive")

    def __init__(self, amount=0.0):
        Gold._validate_amount_is_positive(amount)

        self.name = "Gold"
        self.category = Category.OTHER
        self.amount = amount

    def add_amount(self, amount):
        Gold._validate_amount_is_positive(amount)
        self.amount += amount

    def remove_amount(self, amount):
        Gold._validate_amount_is_positive(amount)

        if amount >= self.amount:
            raise ValueError("Not enough gold")

        self.amount -= amount

    def calculate_weight(self):
        return self.amount / 1000

    def print(self):
        print("Name: " + self.name)
        print("Category: " + self.category.value)
        print("Amount: " + str(self.amount))
        print("Weight: " + str(self.calculate_weight()))
