import tweepy
from googletrans import Translator

from nltk.sentiment.vader import SentimentIntensityAnalyzer

API_KEY = 'fmELU0OJygaMKGM3s5SqGfTN8'
API_SECRET_KEY = 'BLeAPUlQHBCfrS7AQja55kzyhSkDx5wy3iaBhtkkfWkBfKPV1i'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAPxxYQEAAAAAlt6fpt27Z%2FzA9VNEssVMVh4%2BdnU%3DM71C92eMfEGf05BVu8nsGc9fKVaQFqVrF4TBSrzD6WC31oQvAI'

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


