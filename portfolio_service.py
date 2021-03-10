from currency_service import CurrencyService
from coinbase.wallet.model import Account
from position import Position
from currency import Currency
from client_service import ClientService


class PortfolioService:

    @staticmethod
    def get_accounts():
        client = ClientService.get_client()
        accounts = client.get_accounts()['data']
        return list(filter(lambda a: float(
            a['balance']['amount']) > 0, accounts))

    @staticmethod
    def get_positions():
        return [Position(CurrencyService.get_currency(a['balance']['currency']),
                         float(a['balance']['amount']))
                for a in PortfolioService.get_accounts()]
