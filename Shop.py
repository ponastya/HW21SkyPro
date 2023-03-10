from BasicStore import BasicStore
from exceptions import ToManyDifferentProductsError, NotEnoughSpaceError


class Shop(BasicStore):
    def __init__(self, items: dict[str, int], capacity: int = 20):
       super().__init__(items, capacity)

    def add(self, name, amount):
        if self.get_unique_items_count() >= 5:
            raise ToManyDifferentProductsError

        super().add(name, amount)