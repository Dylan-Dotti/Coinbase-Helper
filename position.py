from currency import Currency


class Position:
    def __init__(self, currency: Currency,
                 quantity: float, purchase_total: float) -> None:
        self._currency = currency
        self._quantity = quantity
        self._purchase_total = purchase_total

    def get_currency(self) -> Currency:
        return self._currency

    def get_quantity(self) -> float:
        return self._quantity

    def get_purchase_total(self) -> float:
        return self._purchase_total

    def get_avg_purchase_price(self) -> float:
        return self._purchase_total / self._quantity

    def get_total_value(self) -> float:
        return self._currency.get_price() * self._quantity

    def get_total_profit(self) -> float:
        return self.get_total_value() - self.get_purchase_total()

    def get_percentage_gain(self) -> float:
        self.get_total_profit() / self.get_purchase_total() * 100
