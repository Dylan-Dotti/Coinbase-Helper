from typing import List
from transaction_service import TransactionService
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
        accounts = PortfolioService.get_accounts()
        acct_purchase_totals = PortfolioService._get_account_purchase_totals(
            accounts)
        return [Position(CurrencyService.get_currency(
            a['balance']['currency']),
            float(a['balance']['amount']),
            pt)
            for a, pt in zip(accounts, acct_purchase_totals)]

    @staticmethod
    def get_portfolio_total_position():
        positions = PortfolioService.get_positions()
        return Position(CurrencyService.get_currency('USD'),
                        sum([p.get_total_value() for p in positions]),
                        sum([p.get_purchase_total() for p in positions]))

    @staticmethod
    def _get_account_purchase_totals(accounts) -> List[float]:
        account_purchase_totals = []
        for account in accounts:
            transactions = TransactionService.get_transactions(account['id'])
            transaction_values = map(lambda t: t.get_value_usd(), transactions)
            account_purchase_total = sum(transaction_values)
            account_purchase_totals.append(account_purchase_total)
        return account_purchase_totals
