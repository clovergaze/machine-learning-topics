class Item:
    def __init__(self, name, description, category, value, weight, condition=100.0):
        self.name = name
        self.description = description
        self.category = category
        self.value = value
        self.weight = weight
        self.condition = condition

    def decrease_condition(self, amount):
        self.condition -= amount

    def repair_condition(self):
        self.condition = 100.0

    def print(self):
        print("Name: " + self.name)
        print("Description: " + self.description)
        print("Category: " + self.category.value)
        print("Value: " + str(self.value))
        print("Weight: " + str(self.weight))

        if self.condition > 95.0:
            verbatim = "excellent"
        elif self.condition > 75.0:
            verbatim = "good"
        elif self.condition > 50.0:
            verbatim = "fair"
        elif self.condition > 25.0:
            verbatim = "poor"
        elif self.condition > 0.0:
            verbatim = "very poor"
        else:
            verbatim = "broken"

        print("Condition: " + verbatim + " (" + str(self.condition) + "%)")
