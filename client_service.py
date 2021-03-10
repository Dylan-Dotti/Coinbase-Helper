from coinbase.wallet.client import Client
import os


class ClientService:
    __client: Client = None

    @staticmethod
    def get_client() -> Client:
        return ClientService.__client

    @staticmethod
    def login() -> Client:
        print('Connecting...')
        ClientService.__client = Client(
            os.environ.get('CB_AK'), os.environ.get('CB_SK'))
        print('Connected')
        return ClientService.get_client()
