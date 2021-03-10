from typing import List
from client_service import ClientService
from transaction import Transaction


class TransactionService:

    @staticmethod
    def get_transactions(account_id) -> List[Transaction]:
        client = ClientService.get_client()
        transactions = []
        for trans_data in client.get_transactions(account_id)['data']:
            id = trans_data['id']
            currency = trans_data['amount']['currency']
            quantity = float(trans_data['amount']['amount'])
            value_usd = float(trans_data['native_amount']['amount'])
            trans_type = trans_data['type']
            trans_date = trans_data['created_at']
            status = trans_data['status']
            transactions.append(
                Transaction(id, currency, quantity,
                            value_usd, trans_type, trans_date, status))
        return transactions
