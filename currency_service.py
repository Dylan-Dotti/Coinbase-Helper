from coinbase.wallet.client import Client
from client_service import ClientService
from currency import Currency


class CurrencyService:

    @staticmethod
    def get_currency(name: str) -> Currency:
        if name == 'USD':
            return Currency('USD', 1.00)
        client = ClientService.get_client()
        exchange_string = name + '-USD'
        price = float(client.get_buy_price(
            currency_pair=exchange_string)['amount'])
        return Currency(name, price)


if __name__ == '__main__':
    ClientService.login()
    currency = CurrencyService.get_currency('USD')
    print(currency.get_price())
