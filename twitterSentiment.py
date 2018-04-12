import tweepy
from textblob import TextBlob


consumer_key = 'wpNeJKlizXoEXQFOaSBeC6KCu'
consumer_secret = 'OsvxqIobKP0DSkv08xXUln4tNyIR1GFcWuIeNAjCsQ9SRgCMct'

access_token = '911795246568050690-HYJuKS3GhwxYeTywuL5jGZkUOE7vyR8'
access_token_secret = 'OFPO8QhPh1uhvwlMgQbijjNUWaocawAgBob4C1mMHcnXg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('juventus')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)