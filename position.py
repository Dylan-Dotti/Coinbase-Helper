from currency import Currency


class Position:
    def __init__(self, currency: Currency, quantity: float) -> None:
        self._currency = currency
        self._quantity = quantity

    def get_currency(self) -> Currency:
        return self._currency

    def get_quantity(self) -> float:
        return self._quantity

    def get_total_value(self) -> float:
        return self._currency.get_price() * self._quantity
