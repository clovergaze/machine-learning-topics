from .inventory import Inventory


class Character:
    def __init__(self, name, health=100, inventory=None):
        self.name = name
        self.inventory = inventory if inventory is not None else Inventory()
        self.health = health

    def increase_health(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def print(self):
        print("Name: " + self.name)

        if self.health > 95:
            verbatim = "excellent"
        elif self.health > 75:
            verbatim = "good"
        elif self.health > 50:
            verbatim = "fair"
        elif self.health > 25:
            verbatim = "poor"
        elif self.health > 0:
            verbatim = "very poor"
        else:
            verbatim = "dead"

        print("Health: " + verbatim + " (" + str(self.health) + "%)")
        print()
        self.inventory.print()
