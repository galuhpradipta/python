import tweepy
from textblob import TextBlob


consumer_key = 'O52CsoEb2lddRINwAR0wKzTai'
consumer_secret = 'OOH14xGdkV7oivwvlqJdfF61FzWlf0euUVTb0ODHqn59N7QXrC'

access_token = '294500888-43JnEsyaellp8ZXmOoVvNfaXCl4xWZab6AmbJqz8'
access_token_secret = '8RXRR2YeO3ncN1I5hXH950C2z5HATMwCQ9vg1UtbUwJqS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('juventus')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)