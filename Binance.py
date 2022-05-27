import time
from binance.client import Client
from binance import ThreadedWebsocketManager

API_KEY = "oTLiACHSP1RVqdDuMV34LSE4oTXVHqXU2KKxQ7q9LVs4zkVYxq0OJkbLEDTjzWcG"
SECRET_KEY = "QCJ2MWLBIBGvUt8nZ05SZtiqa9GIvfSHJKltxQKDeW0OKsySJp9MMb514J3pUo6v"

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