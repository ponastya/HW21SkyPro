from Store import Store
from Shop import Shop
from Request import Request
from exceptions import BaseError

store1 = Store(
    items = {
        "банан": 10,
        "яблоко":15
    },
    capacity=150
)

shop1 = Shop(
    items={"банан": 5},
    capacity=100
)

storages = {
    "магазин": shop1,
    "склад": store1
}
print(f"В магазине в наличии: {shop1.get_items()}")
print(f"На складе в наличии: {store1.get_items()}")


while True:
    try:
        request_user = input('''Введите запрос в формате:\n"Доставить 30 банан из склад в магазин"\n''')
        request = Request(request_user, storages)
        request.move()
        print(f"В магазине в наличии: {shop1.get_items()}")
        print(f"На складе в наличии: {store1.get_items()}")

    except BaseError as error:
        print(error.message)
