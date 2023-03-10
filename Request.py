from Store import Store
from Shop import Shop
from exceptions import InvalidRequestError, UnknownStorageError


class Request:
    def __init__(self, request, storages):
        # Доставить 3 печеньки из склад в магазин
        split_req = request.lower().split()

        if len(split_req) != 7 or not split_req[1].isdigit():
            raise InvalidRequestError

        self.from_ = split_req[4]
        self.to = split_req[6]
        self.amount = int(split_req[1])
        self.product = split_req[2]

        self.from__ = storages[self.from_]
        self.to_ = storages[self.to]


    def move(self):
        self.from__.remove(self.product, self.amount)
        print(f"Курьер из {self.from_} увез {self.amount} {self.product}")
        self.to_.add(self.product, self.amount)
        print(f"...")
        print(f"Курьер в {self.to} доставил {self.amount} {self.product}")

