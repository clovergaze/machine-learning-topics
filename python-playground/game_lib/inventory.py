from .gold import Gold


class Inventory:
    def __init__(self, items=None, gold_amount=0):
        self.items = items if items is not None else []
        self.gold = Gold(gold_amount)

    def add_item(self, item):
        if item in self.items:
            raise ValueError("Item already in inventory")
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items:
            raise ValueError("Item not in inventory")
        self.items.remove(item)

    def print(self, category=None):
        print("Inventory")
        print("=========")
        print()
        print("Gold: " + str(self.gold.amount))
        print()
        self._print_items(category)
        print()

    def _print_items(self, category=None):
        if len(self.items) == 0:
            print("Inventory is empty")
        else:
            if category is None:
                for item in self.items:
                    item.print()
                    print()
            else:
                for item in self.items:
                    if item.category == category:
                        item.print()
                        print()
