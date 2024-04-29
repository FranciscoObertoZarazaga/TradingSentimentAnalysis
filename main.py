# https://pypi.org/project/lunarcrush/
# https://legacy.lunarcrush.com/developers/docs
from NewsSearcher import NewsSearcher
from CoinSearcher import CoinSearcher
from Binance import Binance

cs = CoinSearcher()
coins = cs.get_coins()
print(coins)
#coins = cs.filter_coins(coins)


exit()
symbol = 'LTC' #str.upper(input('Ingrese una moneda: '))
limit = 100 # int(input('Ingrese cantidad: '))
ns = NewsSearcher()
ns.print_news(symbol=symbol, limit=limit)
