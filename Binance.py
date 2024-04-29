import time
from binance.client import Client
from binance import ThreadedWebsocketManager

API_KEY = ""
SECRET_KEY = ""

class Binance:

    def __init__(self):
        self.client = Client(API_KEY, SECRET_KEY)

    #Retorna un listado de cryptomonedas disponibles en Binance
    def getAllCoins(self):
        ticker = self.client.get_all_tickers()
        coins = list()
        for symbol in ticker:
            coin = symbol['symbol']
            if 'USDT' == coin[-4:]:
                coins.append(symbol['symbol'].replace('USDT', ''))
        return coins

    def get_client(self):
        return self.client
