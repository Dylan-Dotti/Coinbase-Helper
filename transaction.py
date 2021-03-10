
class Transaction:
    def __init__(self, id: str, currency: str,
                 quantity: float, value_usd: float,
                 trans_type: str, trans_date: str,
                 status: str) -> None:
        self._id = id
        self._currency = currency
        self._quantity = quantity
        self._value_usd = value_usd
        self._trans_type = trans_type
        self._trans_date = trans_date
        self._status = status

    def __str__(self) -> str:
        return ('Exchanged ${value_usd} USD for {quantity} {currency} on {date}'
                .format(value_usd=self._value_usd, quantity=self._quantity,
                        currency=self._currency, date=self._trans_date))

    def get_id(self):
        return self._id

    def get_currency_name(self):
        return self._currency

    def get_quantity(self):
        return self._quantity

    def get_value_usd(self):
        return self._value_usd

    def get_type(self):
        return self._trans_type

    def get_date(self):
        return self._trans_date

    def get_status(self):
        return self._status
