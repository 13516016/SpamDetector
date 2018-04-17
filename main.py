from StringMatcher import KMP, BoyerMoore
from TweetGetter import TweetGetter
from flask import Flask
from flask import redirect, url_for, request, render_template
import json
import re

app = Flask(__name__)
api = TweetGetter('credentials.json')

@app.route('/regex', methods=['POST'])
def evaluateRegex():
	if (request.is_json):
		content = request.get_json()

		# construct pattern from spam word 
		# (the pattern is ".*pattern1.*pattern2.*pattern3 (.......).*patternN .*")
		spam = content['spamkey'].split(' ')
		pattern = '(.*)' + '(.*)'.join(spam) + '(.*)'

		# get tweets based on search key
		tweets = api.search_tweets(content['searchkey'])

		for tweet in tweets:
			if (re.search(pattern, tweet['text'].lower())):
				tweet['is_spam'] = True
			else:
				tweet['is_spam'] = False
			
		return json.dumps(tweets);
	else:
		return "Bad Request"

@app.route('/kmp', methods=['POST'])
def evaluateKMP():
	if (request.is_json):
		content = request.get_json()
		# construct string matcher
		pattern = content['spamkey']
		matcher = KMP(pattern)
		# get tweets based on search key
		tweets = api.search_tweets(content['searchkey'])
		# Evaluate tweets using matcher
		for tweet in tweets:
			tweet['is_spam'] = matcher.match(tweet['text'].lower())
			
		return json.dumps(tweets);
	else:
		return "Bad Request"

@app.route('/bm', methods=['POST'])
def evaluateBM():
	if (request.is_json):
		content = request.get_json()
		# construct string matcher
		pattern = content['spamkey']
		matcher = BoyerMoore(pattern)
		# get tweets based on search key
		tweets = api.search_tweets(content['searchkey'])
		# Evaluate tweets using matcher
		for tweet in tweets:
			tweet['is_spam'] = matcher.match(tweet['text'].lower())

		return json.dumps(tweets);
	else:
		return "Bad Request"

if __name__ == '__main__':
	app.debug = True
	app.run()