from transaction import Transaction
from portfolio_service import PortfolioService
from client_service import ClientService
from transaction_service import TransactionService
import json


def print_positions(positions):
    for pos in positions:
        currency = pos.get_currency()
        print("Currency: ", currency.get_name())
        print("Quantity: ", pos.get_quantity())
        print("Current Price: ", currency.get_price())
        print("Total Value: ", pos.get_total_value())
        print()


client = ClientService.login()

positions = PortfolioService.get_positions()
positions_total_value: float = sum(
    map(lambda p: p.get_total_value(), positions))

accounts = PortfolioService.get_accounts()
account_purchase_total = 0
for account in accounts:
    transactions = TransactionService.get_transactions(account['id'])
    transaction_values = map(lambda t: t.get_value_usd(), transactions)
    transaction_values_sum = sum(transaction_values)
    account_purchase_total += transaction_values_sum
total_profit = positions_total_value - account_purchase_total
print()
print('Account purchase total: $' + str(account_purchase_total))
print('Account current total: $' + str(round(positions_total_value, 2)))
print('Total profit: $' + str(round(total_profit, 2)))
print('Percentage gain:', str(round(total_profit /
                                    account_purchase_total * 100, 2)) + '%')
