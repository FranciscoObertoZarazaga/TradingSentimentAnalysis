import tweepy
from googletrans import Translator

from nltk.sentiment.vader import SentimentIntensityAnalyzer

API_KEY = ''
API_SECRET_KEY = ''
BEARER_TOKEN = ''

client = tweepy.Client(bearer_token=BEARER_TOKEN,consumer_key=API_KEY, consumer_secret=API_SECRET_KEY)
tweets = client.search_recent_tweets(query='bitcoin', max_results=10)[0]
for i in tweets:
    print(i)
print(len(tweets))
exit()
sid = SentimentIntensityAnalyzer()

for tweet in tweets:
    print("-"*50)
    tweet = str(tweet.encode('utf-8'))
    print(tweet)
    print('SCORE:', sid.polarity_scores(tweet))


