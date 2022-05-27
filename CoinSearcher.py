from LunarCrush import LunarCrushClass
from Binance import Binance
import datetime

lc = LunarCrushClass()
binance = Binance()
symbols = binance.getAllCoins()
print('Coin of the day:', lc.get_coin_of_day()[0])

coins = list()
data = lc.get_meta()['data']
for coin in data:
    coin = coin['symbol']
    if coin in symbols:
        coins.append(coin)

print('Cantidad monedas en Binance y LC:', len(coins))
good = list()
for coin in coins:
    try:
        asset_data = lc.get_asset_data(coin)

        price_score = asset_data['price_score']
        social_impact_score = asset_data['social_impact_score']
        average_sentiment = asset_data['average_sentiment']
        correlation_rank = asset_data['correlation_rank']
        volatility = asset_data['volatility']
        galaxy_score = asset_data['galaxy_score']
        time = datetime.datetime.fromtimestamp(asset_data['time'])
        points = (price_score + social_impact_score + average_sentiment) * (correlation_rank/5) / 3

        if points > 5:
            print(f"{coin}:")
            print(f"price_score: {price_score}")
            print(f"social_impact_score: {social_impact_score}")
            print(f"average_sentiment: {average_sentiment}")
            print(f"correlation_rank: {correlation_rank}")
            print(f"volatility: {volatility}")
            print(f"galaxy_score: {galaxy_score}")
            print(f"time: {time}")

            good.append(coin)
    except Exception as e:
        continue

print(f'Monedas filtradas({len(good)}):', good)