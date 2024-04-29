import pandas as pd

from LunarCrush import LunarCrushClass
import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_vars(new):
    new_id = new['id']
    title = new['title']
    publisher = new['publisher']
    url = new['url']
    description = new['description']
    social_score = new['social_score']
    sentiment = new['sentiment']
    #verified = new['verified']
    time = datetime.datetime.fromtimestamp(new['time'])

    return new_id, title, publisher, url, description, social_score, sentiment, time

def get_df(data):
    dic = {
            'title': data[1],
            'publisher': data[2],
            #'verified': data[7],
            'url': data[3],
            'description': data[4],
            'sentiment': data[6],
            'time': data[7]
        }
    df = pd.DataFrame(dic, columns=dic.keys(), index=[0])
    return dic



def search(func):
    def wrapper(self, symbol, limit):
        data = self.lc.get_social(symbol=symbol, limit=limit)
        data.sort_values('time', inplace=True, ignore_index=True)
        return func(self, data)

    return wrapper


class NewsSearcher:

    def __init__(self):
        self.lc = LunarCrushClass()

    @search
    def get_news(self, data):
        df = pd.DataFrame()
        for info in data.iterrows():
            new = info[1]
            new_dic = get_df(get_vars(new))
            new_df = pd.DataFrame(new_dic, columns=new_dic.keys(), index=[0])
            df = pd.concat([df, new_df], ignore_index=True)
        return df

