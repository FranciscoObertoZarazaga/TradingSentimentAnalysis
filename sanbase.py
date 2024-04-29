import san
from datetime import datetime, timedelta

metrics = [
    'twitter_followers',
    'social_dominance_telegram',
    'social_dominance_reddit',
    'social_dominance_total',
    'social_volume_telegram',
    'social_volume_reddit',
    'social_volume_twitter',
    'social_volume_bitcointalk',
    'social_volume_total',
    'community_messages_count_telegram',
    'community_messages_count_total',
    'sentiment_positive_total',
    'sentiment_positive_telegram',
    'sentiment_positive_reddit',
    'sentiment_positive_twitter',
    'sentiment_positive_bitcointalk',
    'sentiment_negative_total',
    'sentiment_negative_telegram',
    'sentiment_negative_reddit',
    'sentiment_negative_twitter',
    'sentiment_negative_bitcointalk',
    'sentiment_balance_total',
    'sentiment_balance_telegram',
    'sentiment_balance_reddit',
    'sentiment_balance_twitter',
    'sentiment_balance_bitcointalk',
    'sentiment_volume_consumed_total',
    'sentiment_volume_consumed_telegram',
    'sentiment_volume_consumed_reddit',
    'sentiment_volume_consumed_twitter',
    'sentiment_volume_consumed_bitcointalk',
]


from_date = (datetime.now().date() - timedelta(days=3)).strftime('%Y-%m-%d')
to_date = (datetime.now().date()).strftime('%Y-%m-%d')

san.ApiConfig.api_key = ''

for metric in metrics:
    try:
        result = san.get(
            f"{metric}/bitcoin",
            from_date=from_date,
            to_date=to_date,
            interval="3d"
        )
        print(metric, result.iloc[0].value)
    except Exception as e:
        continue
