import pandas as pd
from NewsSearcher import NewsSearcher
from LunarCrush import LunarCrushClass
from Binance import Binance
import datetime

class CoinSearcher:

    def __init__(self):
        self.lc = LunarCrushClass()
        self.binance = Binance()
        print('Coin of the day:', self.lc.get_coin_of_day()[0])

    def get_coins(self):
        symbols = self.binance.getAllCoins()
        coins = list()
        data = self.lc.get_meta()['data']
        for coin in data:
            coin = coin['symbol']
            if coin in symbols:
                coins.append(coin)

        print('Cantidad monedas en Binance y LunarCrush:', len(coins))

        df = pd.DataFrame()
        for coin in coins:
            try:
                asset_data = self.lc.get_asset_data(coin)

                coin_dict = {
                    'name': coin,
                    'time': datetime.datetime.fromtimestamp(asset_data['time']),
                    'volatility': asset_data['volatility'] * 100
                }

                coin_df = pd.DataFrame(coin_dict, columns=coin_dict.keys(), index=[0])
                df = pd.concat([df, coin_df], ignore_index=True)
            except Exception as e:
                continue

        df.sort_values('volatility', inplace=True, ignore_index=True, ascending=False)
        print(f'Monedas filtradas: {len(df)}')
        return df

    def filter_coins(self, coins):
        ns = NewsSearcher()
        for coin in coins['name']:
            try:
                print(ns.get_news(symbol=coin, limit=10))
            except Exception as e:
                print(e)



