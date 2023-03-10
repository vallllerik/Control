class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.name, []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)



class Items:
    def __init__(self, name, cost, shop):
        self.name = name
        self.make = cost
        self.year = shop

    def __repr__(self):
        return f'{self.name}-{self.cost}-{self.shop}'


class Item(Items):
    def __init__(self, name, shop, cost):
        super().__init__(name, cost, shop)
        self.name = name




def main():
    sklad = Sklad()
    item_s = Item('Magic Stick', 100, 'Walmart')
    sklad.add_to(item_s)
    print(sklad._dict)
