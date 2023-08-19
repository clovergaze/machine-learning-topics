import uuid

from .inventory import Inventory


class Character:
    def __init__(self, name, health=100, inventory=None):
        self.id = uuid.uuid4()
        self.name = name
        self.inventory = inventory if inventory is not None else Inventory()
        self.health = health

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def increase_health(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    def describe_health(self):
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

        return verbatim + " (" + str(self.health) + "%)"

    def print(self):
        print("Name: " + self.name)
        print("Health: " + self.describe_health())
        print()
        self.inventory.print()
