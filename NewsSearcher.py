from LunarCrush import LunarCrushClass
import datetime

def get_vars(new):
    new_id = new['id']
    title = new['title']
    publisher = new['publisher']
    url = new['url']
    description = new['description']
    social_score = new['social_score']
    sentiment = new['sentiment']
    verified = new['verified']
    time = datetime.datetime.fromtimestamp(new['time'])

    return new_id, title, publisher, url, description, social_score, sentiment, verified, time

def print_new(data):
    print(f'title: "{data[1]}"')
    print(f'publisher: {data[2]}')
    print(f'verified: {data[7]}')
    print(f'url: {data[3]}')
    print(f'description: {data[4]}')
    print(f'sentiment: {data[6]}')
    print(f'time: {data[8]}')
    print('-' * 50)

def search(func):
    def wrapper(self, symbol, limit):
        data = self.lc.get_social(symbol=symbol, limit=limit)
        data.sort_values('time', inplace=True, ignore_index=True)
        func(self, data)
        print(f'Se solicitaron {limit} datos sobre {symbol}')
    return wrapper


class NewsSearcher:

    def __init__(self):
        self.lc = LunarCrushClass()

    @search
    def print_news(self, data):
        for info in data.iterrows():
            new = info[1]
            print_new(get_vars(new))
        print(f'{len(data)} noticias procesadas')

