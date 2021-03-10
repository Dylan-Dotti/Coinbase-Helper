
class Currency:
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price
