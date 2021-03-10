from coinbase.wallet.client import Client
from client_service import ClientService
from currency import Currency


class CurrencyService:

    @staticmethod
    def get_currency(name: str) -> Currency:
        client = ClientService.get_client()
        exchange_string = name + '-USD'
        price = float(client.get_buy_price(
            currency_pair=exchange_string)['amount'])
        return Currency(name, price)
