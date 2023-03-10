from BasicStore import BasicStore



class Store(BasicStore):
    # capacity - максимальная вместимость склада по всем позициям
    def __init__(self, items: dict[str, int], capacity=100):
       super().__init__(items, capacity)
