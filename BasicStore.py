from Storage import Storage
from exceptions import *

class BasicStore(Storage):
    def __init__(self, items: dict[str, int], capacity:int):
       self.items = items
       self.capacity = capacity

    def add(self, name, quantity):
        if self.get_free_space() > quantity:
            if name not in self.items:
                self.items[name] = quantity
            else:
                self.items[name] += quantity
        else:
            raise NotEnoughSpaceError

    def remove(self, name, amount):
        if name not in self.items:
            raise UnknownProductError

        if self.items[name] > 0 and self.items[name] >= amount:
            self.items[name] -= amount
        else:
            raise NotEnoughProductError

    def get_free_space(self):
        sum = 0
        for k, v in self.items.items():
            sum += v
        return self.capacity - sum

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)




