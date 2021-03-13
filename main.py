from position import Position
from transaction import Transaction
from portfolio_service import PortfolioService
from client_service import ClientService
from transaction_service import TransactionService


def print_positions(positions):
    for pos in positions:
        currency = pos.get_currency()
        print("Currency: ", currency.get_name())
        print("Quantity: ", pos.get_quantity())
        print("Current Price: ", currency.get_price())
        print("Total Value: ", pos.get_total_value())
        print()


def print_position_stats(pos: Position) -> None:
    print('Avg purchase price: $' + str(round(pos.get_avg_purchase_price(), 2)))
    print('Purchase total: $' + str(pos.get_purchase_total()))
    print('Current total: $' + str(round(pos.get_total_value(), 2)))
    print('Total profit: $' + str(round(pos.get_total_profit(), 2)))
    print('Percentage gain:', str(round(pos.get_total_profit() /
                                        pos.get_purchase_total() * 100, 2)) + '%')


client = ClientService.login()
print()
positions = PortfolioService.get_positions()
for pos in positions:
    print(pos.get_currency().get_name(), 'statistics:')
    print_position_stats(pos)
    print()
print('Portfolio total statistics:')
account_total = PortfolioService.get_portfolio_total_position()
print_position_stats(account_total)
print()
