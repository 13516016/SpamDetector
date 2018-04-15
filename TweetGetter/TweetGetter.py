import json
import tweepy
import os
from pprint import pprint

# import credentials
class TweetGetter:
	def __init__(self,filename):
		credentials = json.load(open(filename))
		consumer_key = credentials['consumer_key']
		consumer_secret = credentials['consumer_secret']
		access_key = credentials['access_token']
		access_secret = credentials['access_token_secret']
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_key,access_secret)
		api = tweepy.API(auth)
		self.api = api

	def __dictify(self, tweets_object):
		return [{'text':tweet.text, 'screen_name' : tweet.user.screen_name, 'full_name' : tweet.user.name} for tweet in tweets_object]

	def get_timeline_tweets(self):
		tweets_object = self.api.home_timeline(count=10)
		tweets = self.__dictify(tweets_object)	
		return tweets

	def search_tweets(self, query):
		tweets_object = self.api.search(q=query, count=10)
		tweets = self.__dictify(tweets_object)	
		return tweets

