from StringMatcher import KMP
from TweetGetter import TweetGetter
from flask import Flask
from flask import redirect, url_for, request, render_template
import json
import re

app = Flask(__name__)
api = TweetGetter('credentials.json')

@app.route('/kmp', methods=['POST'])
def evaluateKMP():
	if (request.is_json):
		content = request.get_json()
		# construct string matcher
		matcher = KMP(content['spamkey'])
		# get tweets based on search key
		tweets = api.search_tweets(content['searchkey'])
		# Evaluate tweets using matcher
		for tweet in tweets:
			tweet['is_spam'] = matcher.match(tweet['text'])
			
		return json.dumps(tweets);
	else:
		return "Bad Request"

if __name__ == '__main__':
	app.debug = True
	app.run()
	
	# tweets = api.search_tweets("selamat")

	# pprint(tweets)