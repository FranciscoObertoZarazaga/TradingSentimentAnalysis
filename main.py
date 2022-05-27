# https://pypi.org/project/lunarcrush/
# https://legacy.lunarcrush.com/developers/docs
from NewsSearcher import NewsSearcher

symbol = str.upper(input('Ingrese una moneda: '))
limit = int(input('Ingrese cantidad: '))
ns = NewsSearcher()
ns.print_news(symbol=symbol, limit=limit)


input('Press any key to exit')