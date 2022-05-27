import pandas as pd
from lunarcrush import LunarCrush
from datetime import datetime, timedelta


def get_df(data):
    df = pd.DataFrame(dict(), columns=data[0].keys())
    for i in data:
        i = pd.DataFrame(i, columns=i.keys(), index=[0])
        df = pd.concat([df, i], ignore_index=True)
    return df


class LunarCrushClass:

    def __init__(self):
        self.lc = LunarCrush()

    def get_asset_data(self, symbol):
        asset_data = self.lc.get_assets(symbol=[symbol], data_points=1, interval='day')['data'][0]
        #df_asset_data = get_df(asset_data.pop('timeSeries'))
        return asset_data#, df_asset_data

    def get_global_data(self, symbol):
        global_data = self.lc.get_global()['data']
        df_global_data = get_df(global_data.pop('timeSeries'))
        return global_data, df_global_data

    # obtiene todas las monedas disponibles
    def get_meta(self):
        return self.lc.get_meta()

    def get_coin_of_day(self):
        cot = self.lc.get_coin_of_the_day()['data']['symbol']
        cot_info = self.lc.get_coin_of_the_day_info()['data']['history']
        return cot, cot_info

    def get_social(self, symbol, limit, source='news'):
        feeds = self.lc.get_feeds(symbol=symbol, sources=source, limit=limit, type='Chronologic')
        return get_df(feeds['data'])
